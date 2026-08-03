from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_multiclass_defects.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_multiclass_defects.csv 파일이 없습니다."
    )

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

feature_columns = [
    "recipe",
    "chamber_id",
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
    "particle_count",
    "etch_rate_nm_min",
    "uniformity_percent",
]

x = sensor_df[feature_columns]
y = sensor_df["defect_type"]

train_index, test_index = train_test_split(
    np.arange(len(sensor_df)),
    test_size=0.25,
    random_state=42,
    stratify=y,
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
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])
dense_pre = ColumnTransformer([
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
])

models = {
    "LogisticRegression": Pipeline([
        ("preprocess", linear_pre),
        (
            "classifier",
            LogisticRegression(
                max_iter=2000,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ]),
    "RandomForest": Pipeline([
        ("preprocess", tree_pre),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=400,
                max_depth=10,
                min_samples_leaf=4,
                class_weight="balanced",
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]),
    "HistGradientBoosting": Pipeline([
        ("preprocess", dense_pre),
        (
            "classifier",
            HistGradientBoostingClassifier(
                max_iter=200,
                learning_rate=0.08,
                max_depth=6,
                random_state=42,
            ),
        ),
    ]),
}

metric_rows = []
prediction_df = sensor_df.iloc[test_index][
    ["timestamp", "lot_id", "recipe", "chamber_id", "defect_type"]
].copy()
prediction_df = prediction_df.rename(columns={"defect_type": "actual_class"})

best_model_name = None
best_macro_f1 = -1
best_model = None
best_prediction = None

for model_name, model in models.items():
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)

    macro_f1 = f1_score(y_test, prediction, average="macro")
    metric_rows.append({
        "model": model_name,
        "accuracy": accuracy_score(y_test, prediction),
        "macro_f1": macro_f1,
        "weighted_f1": f1_score(y_test, prediction, average="weighted"),
    })

    prediction_df[f"{model_name}_prediction"] = prediction

    if macro_f1 > best_macro_f1:
        best_macro_f1 = macro_f1
        best_model_name = model_name
        best_model = model
        best_prediction = prediction

metrics_df = pd.DataFrame(metric_rows).sort_values("macro_f1", ascending=False)

class_report = classification_report(
    y_test,
    best_prediction,
    output_dict=True,
    zero_division=0,
)
class_metrics_df = pd.DataFrame(class_report).T

labels = best_model.classes_
matrix_df = pd.DataFrame(
    confusion_matrix(y_test, best_prediction, labels=labels),
    index=[f"actual_{label}" for label in labels],
    columns=[f"predicted_{label}" for label in labels],
)

prediction_df["best_model"] = best_model_name
prediction_df["best_prediction"] = best_prediction
misclassified_df = prediction_df.loc[
    prediction_df["actual_class"] != prediction_df["best_prediction"]
].copy()

if best_model_name == "RandomForest":
    feature_names = best_model.named_steps["preprocess"].get_feature_names_out()
    importance = best_model.named_steps["classifier"].feature_importances_
    importance_df = pd.DataFrame({
        "feature": feature_names,
        "importance": importance,
    }).sort_values("importance", ascending=False)
else:
    importance_df = pd.DataFrame({
        "feature": [],
        "importance": [],
    })

excel_file = OUTPUT_DIR / "ex140_multiclass_report.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    metrics_df.to_excel(writer, sheet_name="model_metrics", index=False)
    class_metrics_df.to_excel(writer, sheet_name="class_metrics")
    matrix_df.to_excel(writer, sheet_name="confusion_matrix")
    prediction_df.to_excel(writer, sheet_name="predictions", index=False)
    misclassified_df.to_excel(writer, sheet_name="misclassified_rows", index=False)
    importance_df.to_excel(writer, sheet_name="feature_importance", index=False)

metrics_df.to_csv(
    OUTPUT_DIR / "ex140_model_metrics.csv",
    index=False,
    encoding="utf-8-sig",
)

print(metrics_df.round(4))
print("최고 모델:", best_model_name)
print("보고서 저장:", excel_file)
