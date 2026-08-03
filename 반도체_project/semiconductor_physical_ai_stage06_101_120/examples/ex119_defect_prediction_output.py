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
probability = model.predict_proba(x_test)[:, 1]
prediction = (probability >= 0.4).astype(int)

result_df = sensor_df.iloc[test_index][
    ["timestamp", "lot_id", "recipe", "chamber_id"]
].copy()
result_df["actual_defect"] = y_test.to_numpy()
result_df["defect_probability"] = probability
result_df["predicted_defect"] = prediction

result_df = result_df.sort_values(
    "defect_probability",
    ascending=False,
)

print(result_df.head(20).round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex119_defect_predictions.csv",
    index=False,
    encoding="utf-8-sig",
)
