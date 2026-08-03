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

preprocessor = ColumnTransformer([
    ("num", "passthrough", feature_columns[2:]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), feature_columns[:2]),
])

model = Pipeline([
    ("preprocess", preprocessor),
    (
        "regressor",
        RandomForestRegressor(
            n_estimators=400,
            max_depth=10,
            min_samples_leaf=4,
            random_state=42,
            n_jobs=-1,
        ),
    ),
])

model.fit(x.iloc[train_index], y.iloc[train_index])
prediction = model.predict(x.iloc[test_index])

result_df = sensor_df.iloc[test_index][
    ["timestamp", "lot_id", "yield_percent"]
].copy()
result_df["prediction"] = prediction
result_df["residual"] = (
    result_df["yield_percent"] - result_df["prediction"]
)
result_df["absolute_residual"] = result_df["residual"].abs()

print("잔차 평균:", round(result_df["residual"].mean(), 4))
print("잔차 표준편차:", round(result_df["residual"].std(), 4))
print("MAE:", round(result_df["absolute_residual"].mean(), 4))

top_df = result_df.sort_values(
    "absolute_residual",
    ascending=False,
).head(20)
top_df.to_csv(
    OUTPUT_DIR / "ex154_large_residuals.csv",
    index=False,
    encoding="utf-8-sig",
)
