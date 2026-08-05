from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

baseline_variance = (
    sensor_df["chamber_temp_c"]
    .iloc[:120]
    .var(ddof=1)
)

sensor_df["temp_rolling_variance_30"] = (
    sensor_df["chamber_temp_c"]
    .rolling(window=30, min_periods=10)
    .var(ddof=1)
)

threshold = baseline_variance * 2.0
sensor_df["variance_alarm"] = (
    sensor_df["temp_rolling_variance_30"] > threshold
)

print("기준 분산:", round(baseline_variance, 5))
print("분산 경보 기준:", round(threshold, 5))
print(
    "최초 분산 경보:",
    sensor_df.loc[
        sensor_df["variance_alarm"],
        "timestamp",
    ].min(),
)
