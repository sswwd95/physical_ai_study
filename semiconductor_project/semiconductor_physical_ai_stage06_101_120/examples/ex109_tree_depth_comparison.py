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
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
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

preprocessor = ColumnTransformer([
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

rows = []
for depth in [2, 3, 5, 8, None]:
    model = Pipeline([
        ("preprocess", preprocessor),
        (
            "classifier",
            DecisionTreeClassifier(
                max_depth=depth,
                min_samples_leaf=5,
                random_state=42,
            ),
        ),
    ])
    model.fit(x_train, y_train)

    rows.append({
        "max_depth": str(depth),
        "train_f1": f1_score(
            y_train,
            model.predict(x_train),
            zero_division=0,
        ),
        "test_f1": f1_score(
            y_test,
            model.predict(x_test),
            zero_division=0,
        ),
    })

result_df = pd.DataFrame(rows)
print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex109_tree_depth_comparison.csv",
    index=False,
    encoding="utf-8-sig",
)
