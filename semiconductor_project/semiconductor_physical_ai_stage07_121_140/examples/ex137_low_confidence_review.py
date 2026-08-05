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
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

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

preprocessor = ColumnTransformer([
    ("num", "passthrough", feature_columns[2:]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), feature_columns[:2]),
])

base_model = Pipeline([
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

model = CalibratedClassifierCV(
    estimator=base_model,
    method="sigmoid",
    cv=3,
)
model.fit(x_train, y_train)

probability = model.predict_proba(x_test)
order = np.argsort(probability, axis=1)[:, ::-1]

top1_index = order[:, 0]
top2_index = order[:, 1]

result_df = sensor_df.iloc[test_index][
    ["timestamp", "lot_id", "defect_type"]
].copy()
result_df["predicted_class"] = model.classes_[top1_index]
result_df["top1_probability"] = probability[
    np.arange(len(probability)),
    top1_index,
]
result_df["top2_class"] = model.classes_[top2_index]
result_df["top2_probability"] = probability[
    np.arange(len(probability)),
    top2_index,
]
result_df["probability_gap"] = (
    result_df["top1_probability"]
    - result_df["top2_probability"]
)
result_df["review_required"] = (
    result_df["top1_probability"] < 0.55
)

print("재검사 대상 수:", int(result_df["review_required"].sum()))
result_df.to_csv(
    OUTPUT_DIR / "ex137_low_confidence_review.csv",
    index=False,
    encoding="utf-8-sig",
)
