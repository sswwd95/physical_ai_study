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

from sklearn.calibration import CalibratedClassifierCV
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(columns=["timestamp", "lot_id", "defect_type"])
y = sensor_df["defect_type"]

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

base_pipeline = Pipeline([
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

calibrated_model = CalibratedClassifierCV(
    estimator=base_pipeline,
    method="sigmoid",
    cv=3,
)
calibrated_model.fit(x_train, y_train)

probability = calibrated_model.predict_proba(x_test)
print("Log loss:", round(log_loss(y_test, probability), 4))
print("클래스 순서:", calibrated_model.classes_)
print(
    "평균 예측확률:",
    np.round(probability.mean(axis=0), 4),
)
