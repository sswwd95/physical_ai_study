from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

rolling_mean = (
    sensor_df["chamber_temp_c"]
    .rolling(window=20, min_periods=10)
    .mean()
)
rolling_std = (
    sensor_df["chamber_temp_c"]
    .rolling(window=20, min_periods=10)
    .std()
)

sensor_df["rolling_residual_z"] = (
    sensor_df["chamber_temp_c"] - rolling_mean
) / rolling_std
sensor_df["rolling_residual_anomaly"] = (
    sensor_df["rolling_residual_z"].abs() >= 3
)

print(
    "이동잔차 이상 수:",
    int(sensor_df["rolling_residual_anomaly"].sum()),
)
