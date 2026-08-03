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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(
    columns=["timestamp", "lot_id", "defect", "defect_type"]
)
y = sensor_df["defect"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42, stratify=y
)

train_df = x_train.copy()
train_df["defect"] = y_train.values

normal_df = train_df.loc[train_df["defect"] == 0]
defect_df = train_df.loc[train_df["defect"] == 1]

defect_oversampled = defect_df.sample(
    n=len(normal_df),
    replace=True,
    random_state=42,
)
balanced_df = pd.concat(
    [normal_df, defect_oversampled],
    ignore_index=True,
).sample(frac=1, random_state=42)

x_train_balanced = balanced_df.drop(columns=["defect"])
y_train_balanced = balanced_df["defect"]

print("오버샘플링 전:")
print(y_train.value_counts())
print("\n오버샘플링 후:")
print(y_train_balanced.value_counts())

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

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

model = Pipeline([
    ("preprocess", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
])

model.fit(x_train_balanced, y_train_balanced)
y_pred = model.predict(x_test)

print("Precision:", round(precision_score(y_test, y_pred, zero_division=0), 4))
print("Recall:", round(recall_score(y_test, y_pred, zero_division=0), 4))
print("F1:", round(f1_score(y_test, y_pred, zero_division=0), 4))
