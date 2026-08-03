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
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

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
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

model = Pipeline([
    ("preprocess", preprocessor),
    (
        "classifier",
        OneVsRestClassifier(
            LogisticRegression(
                max_iter=2000,
                class_weight="balanced",
                random_state=42,
            )
        ),
    ),
])

model.fit(x_train, y_train)

feature_names = model.named_steps["preprocess"].get_feature_names_out()
classifier = model.named_steps["classifier"]

rows = []
for class_name, estimator in zip(classifier.classes_, classifier.estimators_):
    coefficient = estimator.coef_[0]
    order = np.argsort(np.abs(coefficient))[::-1][:8]
    for rank, index in enumerate(order, start=1):
        rows.append({
            "class_name": class_name,
            "rank": rank,
            "feature": feature_names[index],
            "coefficient": coefficient[index],
        })

result_df = pd.DataFrame(rows)
print(result_df.head(20).round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex125_ovr_coefficients.csv",
    index=False,
    encoding="utf-8-sig",
)
