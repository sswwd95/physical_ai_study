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

values = sensor_df["chamber_temp_c"].to_numpy()
window = 20
difference = np.full(len(values), np.nan)

for index in range(window, len(values) - window):
    left_mean = values[index - window:index].mean()
    right_mean = values[index:index + window].mean()
    difference[index] = right_mean - left_mean

sensor_df["local_mean_difference"] = difference
sensor_df["local_change_alarm"] = (
    sensor_df["local_mean_difference"].abs() >= 1.0
)

print(
    "국소 변화 경보 수:",
    int(sensor_df["local_change_alarm"].sum()),
)
sensor_df.to_csv(
    OUTPUT_DIR / "ex072_local_change_detection.csv",
    index=False,
    encoding="utf-8-sig",
)
