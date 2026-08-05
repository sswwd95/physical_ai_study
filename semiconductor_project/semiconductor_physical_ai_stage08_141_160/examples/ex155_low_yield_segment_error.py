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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(columns=["timestamp", "lot_id", "yield_percent"])
y = sensor_df["yield_percent"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)

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

preprocessor = ColumnTransformer([
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

model = Pipeline([
    ("preprocess", preprocessor),
    (
        "regressor",
        RandomForestRegressor(
            n_estimators=400,
            random_state=42,
            n_jobs=-1,
        ),
    ),
])

model.fit(x_train, y_train)
prediction = model.predict(x_test)

low_mask = y_test < 92.0
high_mask = ~low_mask

summary_df = pd.DataFrame([
    {
        "segment": "all",
        "row_count": len(y_test),
        "mae": mean_absolute_error(y_test, prediction),
    },
    {
        "segment": "low_yield",
        "row_count": int(low_mask.sum()),
        "mae": (
            mean_absolute_error(y_test[low_mask], prediction[low_mask])
            if low_mask.any()
            else np.nan
        ),
    },
    {
        "segment": "normal_yield",
        "row_count": int(high_mask.sum()),
        "mae": mean_absolute_error(y_test[high_mask], prediction[high_mask]),
    },
])

print(summary_df.round(4))
summary_df.to_csv(
    OUTPUT_DIR / "ex155_segment_error.csv",
    index=False,
    encoding="utf-8-sig",
)
