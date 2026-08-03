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

baseline = sensor_df["chamber_temp_c"].iloc[:120]
mean_value = baseline.mean()
std_value = baseline.std(ddof=1)

z = (
    sensor_df["chamber_temp_c"] - mean_value
) / std_value

k = 0.5
h = 5.0
cusum_values = []
current = 0.0

for value in z:
    current = max(0.0, current + value - k)
    cusum_values.append(current)

sensor_df["cusum_upper"] = cusum_values
sensor_df["cusum_upper_alarm"] = (
    sensor_df["cusum_upper"] >= h
)

print(
    "상방 CUSUM 최초 경보 시점:",
    sensor_df.loc[
        sensor_df["cusum_upper_alarm"],
        "timestamp",
    ].min(),
)
sensor_df.to_csv(
    OUTPUT_DIR / "ex063_upper_cusum_temperature.csv",
    index=False,
    encoding="utf-8-sig",
)
