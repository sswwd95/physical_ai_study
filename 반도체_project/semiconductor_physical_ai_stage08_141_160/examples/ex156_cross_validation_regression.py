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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(columns=["timestamp", "lot_id", "yield_percent"])
y = sensor_df["yield_percent"]

numeric_features = [
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
categorical_features = ["recipe", "chamber_id"]

preprocessor = ColumnTransformer([
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

model = Pipeline([
    ("preprocess", preprocessor),
    (
        "regressor",
        RandomForestRegressor(
            n_estimators=300,
            random_state=42,
            n_jobs=-1,
        ),
    ),
])

cv = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_validate(
    model,
    x,
    y,
    cv=cv,
    scoring=[
        "neg_mean_absolute_error",
        "neg_root_mean_squared_error",
        "r2",
    ],
)

fold_df = pd.DataFrame({
    "fold": np.arange(1, 6),
    "mae": -scores["test_neg_mean_absolute_error"],
    "rmse": -scores["test_neg_root_mean_squared_error"],
    "r2": scores["test_r2"],
})

summary_df = pd.DataFrame([{
    "fold": "mean",
    "mae": fold_df["mae"].mean(),
    "rmse": fold_df["rmse"].mean(),
    "r2": fold_df["r2"].mean(),
}])

result_df = pd.concat([fold_df, summary_df], ignore_index=True)
print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex156_regression_cv.csv",
    index=False,
    encoding="utf-8-sig",
)
