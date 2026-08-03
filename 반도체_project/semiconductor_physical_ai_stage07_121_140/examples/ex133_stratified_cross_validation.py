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
from sklearn.model_selection import StratifiedKFold, cross_validate
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

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_validate(
    model,
    x,
    y,
    cv=cv,
    scoring=["accuracy", "f1_macro", "f1_weighted"],
)

fold_df = pd.DataFrame({
    "fold": np.arange(1, 6),
    "accuracy": scores["test_accuracy"],
    "macro_f1": scores["test_f1_macro"],
    "weighted_f1": scores["test_f1_weighted"],
})

summary_df = pd.DataFrame([
    {
        "fold": "mean",
        "accuracy": fold_df["accuracy"].mean(),
        "macro_f1": fold_df["macro_f1"].mean(),
        "weighted_f1": fold_df["weighted_f1"].mean(),
    },
    {
        "fold": "std",
        "accuracy": fold_df["accuracy"].std(),
        "macro_f1": fold_df["macro_f1"].std(),
        "weighted_f1": fold_df["weighted_f1"].std(),
    },
])

result_df = pd.concat([fold_df, summary_df], ignore_index=True)
print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex133_multiclass_cv.csv",
    index=False,
    encoding="utf-8-sig",
)
