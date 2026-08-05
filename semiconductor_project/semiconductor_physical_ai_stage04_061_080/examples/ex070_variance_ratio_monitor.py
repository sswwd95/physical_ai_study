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

rolling_variance = (
    sensor_df["chamber_temp_c"]
    .rolling(window=40, min_periods=15)
    .var(ddof=1)
)

sensor_df["variance_ratio"] = (
    rolling_variance / baseline_variance
)
sensor_df["variance_ratio_alarm"] = (
    sensor_df["variance_ratio"] >= 2.5
)

print(
    "분산비 경보 수:",
    int(sensor_df["variance_ratio_alarm"].sum()),
)
sensor_df.to_csv(
    OUTPUT_DIR / "ex070_variance_ratio_monitor.csv",
    index=False,
    encoding="utf-8-sig",
)
