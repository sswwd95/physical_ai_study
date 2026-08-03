from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

sensor_df["temp_rolling_mean_20"] = (
    sensor_df["chamber_temp_c"]
    .rolling(window=20, min_periods=5)
    .mean()
)
sensor_df["temp_rolling_std_20"] = (
    sensor_df["chamber_temp_c"]
    .rolling(window=20, min_periods=5)
    .std()
)

result_df = sensor_df[
    [
        "timestamp",
        "chamber_temp_c",
        "temp_rolling_mean_20",
        "temp_rolling_std_20",
    ]
]

print(result_df.tail(30).round(3))
result_df.to_csv(
    OUTPUT_DIR / "ex043_rolling_mean_std.csv",
    index=False,
    encoding="utf-8-sig",
)
