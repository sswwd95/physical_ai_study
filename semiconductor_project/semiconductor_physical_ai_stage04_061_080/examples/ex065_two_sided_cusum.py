from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

def calculate_two_sided_cusum(values, mean_value, std_value, k=0.5, h=5.0):
    upper_values = []
    lower_values = []
    upper = 0.0
    lower = 0.0

    for raw_value in values:
        z = (raw_value - mean_value) / std_value
        upper = max(0.0, upper + z - k)
        lower = min(0.0, lower + z + k)
        upper_values.append(upper)
        lower_values.append(lower)

    alarm = (
        (np.array(upper_values) >= h)
        | (np.abs(np.array(lower_values)) >= h)
    )
    return upper_values, lower_values, alarm

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

baseline = sensor_df["chamber_temp_c"].iloc[:120]
upper, lower, alarm = calculate_two_sided_cusum(
    sensor_df["chamber_temp_c"].to_numpy(),
    baseline.mean(),
    baseline.std(ddof=1),
)

sensor_df["cusum_upper"] = upper
sensor_df["cusum_lower"] = lower
sensor_df["two_sided_alarm"] = alarm

print("양방향 CUSUM 경보 수:", int(alarm.sum()))
sensor_df.to_csv(
    OUTPUT_DIR / "ex065_two_sided_cusum.csv",
    index=False,
    encoding="utf-8-sig",
)
