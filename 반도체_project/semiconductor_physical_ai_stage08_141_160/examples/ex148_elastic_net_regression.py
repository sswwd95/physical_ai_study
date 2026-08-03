from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_yield_regression.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_yield_regression.csv 파일이 없습니다."
    )

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import ElasticNet, Lasso, Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(columns=["timestamp", "lot_id", "yield_percent"])
y = sensor_df["yield_percent"]

numeric_features = [
    "temp_mean_c",
    "temp_std_c",
    "pressure_mean_pa",
    "pressure_std_pa",
    "rf_power_mean_w",
    "gas_flow_mean_sccm",
    "vibration_rms_g",
    "particle_mean",
    "downtime_min",
    "maintenance_age_hours",
]
categorical_features = ["recipe", "chamber_id"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

regressors = {
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=0.01, max_iter=5000),
    "ElasticNet": ElasticNet(
        alpha=0.01,
        l1_ratio=0.5,
        max_iter=5000,
    ),
}

rows = []
for name, regressor in regressors.items():
    model = Pipeline([
        ("preprocess", preprocessor),
        ("regressor", regressor),
    ])
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    rows.append({
        "model": name,
        "mae": mean_absolute_error(y_test, prediction),
        "r2": r2_score(y_test, prediction),
    })

result_df = pd.DataFrame(rows).sort_values("mae")
print(result_df.round(4))
