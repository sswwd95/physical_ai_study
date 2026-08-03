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
from sklearn.model_selection import StratifiedKFold, cross_validate
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

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

model = Pipeline([
    ("preprocess", preprocessor),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42,
        ),
    ),
])

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42,
)

scores = cross_validate(
    model,
    x,
    y,
    cv=cv,
    scoring=["precision", "recall", "f1"],
)

fold_df = pd.DataFrame({
    "fold": np.arange(1, 6),
    "precision": scores["test_precision"],
    "recall": scores["test_recall"],
    "f1": scores["test_f1"],
})

summary_df = pd.DataFrame([{
    "fold": "mean",
    "precision": fold_df["precision"].mean(),
    "recall": fold_df["recall"].mean(),
    "f1": fold_df["f1"].mean(),
}, {
    "fold": "std",
    "precision": fold_df["precision"].std(),
    "recall": fold_df["recall"].std(),
    "f1": fold_df["f1"].std(),
}])

result_df = pd.concat([fold_df, summary_df], ignore_index=True)
print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex118_cross_validation_scores.csv",
    index=False,
    encoding="utf-8-sig",
)
