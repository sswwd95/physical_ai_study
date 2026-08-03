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
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor

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
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

model = Pipeline([
    ("preprocess", preprocessor),
    (
        "regressor",
        DecisionTreeRegressor(
            max_depth=6,
            min_samples_leaf=10,
            random_state=42,
        ),
    ),
])

model.fit(x_train, y_train)
prediction = model.predict(x_test)

print("MAE:", round(mean_absolute_error(y_test, prediction), 4))
print("RMSE:", round(mean_squared_error(y_test, prediction) ** 0.5, 4))
print("R2:", round(r2_score(y_test, prediction), 4))
