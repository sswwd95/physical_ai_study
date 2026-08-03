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
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
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
    ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
])

pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("classifier", HistGradientBoostingClassifier(random_state=42)),
])

param_distributions = {
    "classifier__learning_rate": [0.03, 0.05, 0.08, 0.12],
    "classifier__max_iter": [100, 200, 300],
    "classifier__max_depth": [3, 5, 7, None],
    "classifier__l2_regularization": [0.0, 0.1, 1.0],
}

search = RandomizedSearchCV(
    pipeline,
    param_distributions=param_distributions,
    n_iter=8,
    scoring="f1_macro",
    cv=3,
    random_state=42,
    n_jobs=-1,
)
search.fit(x_train, y_train)

print("최적 파라미터:", search.best_params_)
print("최적 CV macro F1:", round(search.best_score_, 4))
