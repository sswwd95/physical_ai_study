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
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

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

preprocessor = ColumnTransformer([
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

model = Pipeline([
    ("preprocess", preprocessor),
    (
        "classifier",
        RandomForestClassifier(
            n_estimators=300,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1,
        ),
    ),
])

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

report_df = pd.DataFrame([{
    "tn": tn,
    "fp": fp,
    "fn": fn,
    "tp": tp,
    "specificity": tn / (tn + fp) if tn + fp else 0,
    "false_negative_rate": fn / (fn + tp) if fn + tp else 0,
}])

print(report_df.round(4))
report_df.to_csv(
    OUTPUT_DIR / "ex115_confusion_matrix_analysis.csv",
    index=False,
    encoding="utf-8-sig",
)
