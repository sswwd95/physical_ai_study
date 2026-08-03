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
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

rows = []
for class_weight in [None, "balanced"]:
    model = Pipeline([
        ("preprocess", preprocessor),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight=class_weight,
                random_state=42,
            ),
        ),
    ])
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    rows.append({
        "class_weight": str(class_weight),
        "predicted_defect_count": int(y_pred.sum()),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
    })

result_df = pd.DataFrame(rows)
print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex112_class_weight_comparison.csv",
    index=False,
    encoding="utf-8-sig",
)
