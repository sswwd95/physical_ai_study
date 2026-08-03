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
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(
    columns=["timestamp", "lot_id", "defect", "defect_type"]
)
y = sensor_df["defect"]

numeric_features = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
    "particle_count",
    "etch_rate_nm_min",
    "uniformity_percent",
]
categorical_features = ["recipe", "chamber_id"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42, stratify=y
)

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
                class_weight="balanced",
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]),
}

rows = []
for name, model in models.items():
    model.fit(x_train, y_train)
    probability = model.predict_proba(x_test)[:, 1]
    rows.append({
        "model": name,
        "roc_auc": roc_auc_score(y_test, probability),
    })

result_df = pd.DataFrame(rows).sort_values("roc_auc", ascending=False)
print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex116_roc_auc_comparison.csv",
    index=False,
    encoding="utf-8-sig",
)
