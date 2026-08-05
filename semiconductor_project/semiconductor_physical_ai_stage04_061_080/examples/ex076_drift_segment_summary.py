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
z = (
    sensor_df["chamber_temp_c"] - baseline.mean()
) / baseline.std(ddof=1)

k = 0.5
h = 5.0
values = []
current = 0.0

for value in z:
    current = max(0.0, current + value - k)
    values.append(current)

sensor_df["cusum_alarm"] = np.array(values) >= h

start_flag = (
    sensor_df["cusum_alarm"]
    & ~sensor_df["cusum_alarm"].shift(1, fill_value=False)
)
sensor_df["segment_id"] = start_flag.cumsum()
sensor_df.loc[
    ~sensor_df["cusum_alarm"],
    "segment_id",
] = 0

segment_df = (
    sensor_df.loc[sensor_df["segment_id"] > 0]
    .groupby("segment_id")
    .agg(
        start_time=("timestamp", "min"),
        end_time=("timestamp", "max"),
        length=("timestamp", "size"),
        mean_temperature=("chamber_temp_c", "mean"),
    )
    .reset_index()
)

print(segment_df.round(3))
segment_df.to_csv(
    OUTPUT_DIR / "ex076_drift_segments.csv",
    index=False,
    encoding="utf-8-sig",
)
