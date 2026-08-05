from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_yield_regression.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_yield_regression.csv 파일이 없습니다."
    )

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

feature_columns = [
    "recipe",
    "chamber_id",
    "temp_mean_c",
    "temp_std_c",
    "pressure_mean_pa",
    "pressure_std_pa",
    "rf_power_mean_w",
    "gas_flow_mean_sccm",
    "vibration_rms_g",
    "particle_mean",
    "downtime_min",
    "maintenance_age_hours",
]

x = sensor_df[feature_columns]
y = sensor_df["yield_percent"]

train_index, test_index = train_test_split(
    np.arange(len(sensor_df)),
    test_size=0.25,
    random_state=42,
)

x_train = x.iloc[train_index]
x_test = x.iloc[test_index]
y_train = y.iloc[train_index]
y_test = y.iloc[test_index]

numeric_features = feature_columns[2:]
categorical_features = feature_columns[:2]

linear_pre = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])
tree_pre = ColumnTransformer([
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
])

models = {
    "LinearRegression": Pipeline([
        ("preprocess", linear_pre),
        ("regressor", LinearRegression()),
    ]),
    "Ridge": Pipeline([
        ("preprocess", linear_pre),
        ("regressor", Ridge(alpha=1.0)),
    ]),
    "RandomForest": Pipeline([
        ("preprocess", tree_pre),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=400,
                max_depth=10,
                min_samples_leaf=4,
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]),
    "GradientBoosting": Pipeline([
        ("preprocess", tree_pre),
        (
            "regressor",
            GradientBoostingRegressor(
                n_estimators=250,
                learning_rate=0.05,
                max_depth=3,
                random_state=42,
            ),
        ),
    ]),
}

metric_rows = []
prediction_df = sensor_df.iloc[test_index][
    ["timestamp", "lot_id", "recipe", "chamber_id", "yield_percent"]
].copy()
prediction_df = prediction_df.rename(columns={"yield_percent": "actual_yield"})

best_model_name = None
best_mae = np.inf
best_model = None
best_prediction = None

for model_name, model in models.items():
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)

    mae = mean_absolute_error(y_test, prediction)
    metric_rows.append({
        "model": model_name,
        "mae": mae,
        "rmse": mean_squared_error(y_test, prediction) ** 0.5,
        "r2": r2_score(y_test, prediction),
    })

    prediction_df[f"{model_name}_prediction"] = prediction

    if mae < best_mae:
        best_mae = mae
        best_model_name = model_name
        best_model = model
        best_prediction = prediction

metrics_df = pd.DataFrame(metric_rows).sort_values("mae")

prediction_df["best_model"] = best_model_name
prediction_df["best_prediction"] = best_prediction
prediction_df["residual"] = (
    prediction_df["actual_yield"]
    - prediction_df["best_prediction"]
)
prediction_df["absolute_error"] = prediction_df["residual"].abs()

residual_summary_df = pd.DataFrame([{
    "best_model": best_model_name,
    "residual_mean": prediction_df["residual"].mean(),
    "residual_std": prediction_df["residual"].std(),
    "mae": prediction_df["absolute_error"].mean(),
    "low_yield_actual_count": int(
        (prediction_df["actual_yield"] < 92.0).sum()
    ),
    "low_yield_predicted_count": int(
        (prediction_df["best_prediction"] < 92.0).sum()
    ),
}])

if best_model_name == "RandomForest":
    feature_names = best_model.named_steps["preprocess"].get_feature_names_out()
    importance = best_model.named_steps["regressor"].feature_importances_
    importance_df = pd.DataFrame({
        "feature": feature_names,
        "importance": importance,
    }).sort_values("importance", ascending=False)
else:
    importance_df = pd.DataFrame({
        "feature": [],
        "importance": [],
    })

excel_file = OUTPUT_DIR / "ex160_yield_regression_report.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    metrics_df.to_excel(writer, sheet_name="model_metrics", index=False)
    prediction_df.to_excel(writer, sheet_name="predictions", index=False)
    residual_summary_df.to_excel(writer, sheet_name="residual_summary", index=False)
    importance_df.to_excel(writer, sheet_name="feature_importance", index=False)

metrics_df.to_csv(
    OUTPUT_DIR / "ex160_model_metrics.csv",
    index=False,
    encoding="utf-8-sig",
)

print(metrics_df.round(4))
print("최고 모델:", best_model_name)
print("보고서 저장:", excel_file)
