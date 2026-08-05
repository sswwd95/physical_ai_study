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
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

feature_columns = [
    "recipe",
    "chamber_id",
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

x = sensor_df[feature_columns]
y = sensor_df["yield_percent"]

train_index, test_index = train_test_split(
    np.arange(len(sensor_df)),
    test_size=0.25,
    random_state=42,
)

predictions = []

for seed in range(20):
    preprocessor = ColumnTransformer([
        ("num", "passthrough", feature_columns[2:]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), feature_columns[:2]),
    ])

    model = Pipeline([
        ("preprocess", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=150,
                max_depth=10,
                min_samples_leaf=4,
                random_state=seed,
                n_jobs=-1,
            ),
        ),
    ])

    model.fit(x.iloc[train_index], y.iloc[train_index])
    predictions.append(model.predict(x.iloc[test_index]))

prediction_matrix = np.vstack(predictions)

result_df = sensor_df.iloc[test_index][
    ["timestamp", "lot_id", "yield_percent"]
].copy()
result_df["prediction_p05"] = np.quantile(prediction_matrix, 0.05, axis=0)
result_df["prediction_p50"] = np.quantile(prediction_matrix, 0.50, axis=0)
result_df["prediction_p95"] = np.quantile(prediction_matrix, 0.95, axis=0)

result_df.to_csv(
    OUTPUT_DIR / "ex158_prediction_intervals.csv",
    index=False,
    encoding="utf-8-sig",
)

print(result_df.head(10).round(3))
