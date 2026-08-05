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

preprocessor = ColumnTransformer([
    ("num", "passthrough", feature_columns[2:]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), feature_columns[:2]),
])

model = Pipeline([
    ("preprocess", preprocessor),
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
])

model.fit(x.iloc[train_index], y.iloc[train_index])

probability = model.predict_proba(x.iloc[test_index])
prediction = model.predict(x.iloc[test_index])
classes = model.named_steps["classifier"].classes_

result_df = sensor_df.iloc[test_index][
    ["timestamp", "lot_id", "recipe", "chamber_id", "defect_type"]
].copy()
result_df = result_df.rename(columns={"defect_type": "actual_class"})
result_df["predicted_class"] = prediction
result_df["max_probability"] = probability.max(axis=1)

for class_index, class_name in enumerate(classes):
    result_df[f"probability_{class_name}"] = probability[:, class_index]

result_df = result_df.sort_values(
    "max_probability",
    ascending=False,
)

print(result_df.head(20).round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex139_multiclass_predictions.csv",
    index=False,
    encoding="utf-8-sig",
)
