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

score = np.zeros(len(sensor_df))
for column in [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "vibration_g",
]:
    baseline = sensor_df[column].iloc[:120]
    z = (
        sensor_df[column] - baseline.mean()
    ) / baseline.std(ddof=1)
    score += z.abs()

raw_alarm = score >= 8.0

cooldown = 20
cooldown_alarm = np.zeros(len(sensor_df), dtype=bool)
next_allowed_index = 0

for index, alarm in enumerate(raw_alarm):
    if alarm and index >= next_allowed_index:
        cooldown_alarm[index] = True
        next_allowed_index = index + cooldown

sensor_df["raw_alarm"] = raw_alarm
sensor_df["cooldown_alarm"] = cooldown_alarm

print("원시 경보 수:", int(raw_alarm.sum()))
print("쿨다운 적용 경보 수:", int(cooldown_alarm.sum()))
