from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_defect_classification.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_defect_classification.csv 파일이 없습니다."
    )

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

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
y = sensor_df["defect"]

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

linear_preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

tree_preprocessor = ColumnTransformer([
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

models = {
    "LogisticRegression": Pipeline([
        ("preprocess", linear_preprocessor),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ]),
    "DecisionTree": Pipeline([
        ("preprocess", tree_preprocessor),
        (
            "classifier",
            DecisionTreeClassifier(
                max_depth=5,
                min_samples_leaf=10,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ]),
    "RandomForest": Pipeline([
        ("preprocess", tree_preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=300,
                max_depth=8,
                min_samples_leaf=5,
                class_weight="balanced",
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]),
}

metric_rows = []
confusion_rows = []
prediction_df = sensor_df.iloc[test_index][
    ["timestamp", "lot_id", "recipe", "chamber_id", "defect"]
].copy()
prediction_df = prediction_df.rename(columns={"defect": "actual_defect"})

for model_name, model in models.items():
    model.fit(x_train, y_train)
    probability = model.predict_proba(x_test)[:, 1]
    prediction = (probability >= 0.5).astype(int)

    metric_rows.append({
        "model": model_name,
        "accuracy": accuracy_score(y_test, prediction),
        "precision": precision_score(y_test, prediction, zero_division=0),
        "recall": recall_score(y_test, prediction, zero_division=0),
        "f1": f1_score(y_test, prediction, zero_division=0),
        "roc_auc": roc_auc_score(y_test, probability),
        "pr_auc": average_precision_score(y_test, probability),
    })

    tn, fp, fn, tp = confusion_matrix(y_test, prediction).ravel()
    confusion_rows.append({
        "model": model_name,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "tp": tp,
    })

    prediction_df[f"{model_name}_probability"] = probability
    prediction_df[f"{model_name}_prediction"] = prediction

metrics_df = pd.DataFrame(metric_rows).sort_values("f1", ascending=False)
confusion_df = pd.DataFrame(confusion_rows)

rf_model = models["RandomForest"]
rf_feature_names = rf_model.named_steps["preprocess"].get_feature_names_out()
rf_importance = rf_model.named_steps["classifier"].feature_importances_
importance_df = pd.DataFrame({
    "feature": rf_feature_names,
    "importance": rf_importance,
}).sort_values("importance", ascending=False)

excel_file = OUTPUT_DIR / "ex120_classification_report.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    metrics_df.to_excel(writer, sheet_name="model_metrics", index=False)
    confusion_df.to_excel(writer, sheet_name="confusion_matrices", index=False)
    prediction_df.to_excel(writer, sheet_name="predictions", index=False)
    importance_df.to_excel(writer, sheet_name="feature_importance", index=False)

metrics_df.to_csv(
    OUTPUT_DIR / "ex120_model_metrics.csv",
    index=False,
    encoding="utf-8-sig",
)

print(metrics_df.round(4))
print("보고서 저장:", excel_file)
