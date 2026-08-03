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

temp_mean = sensor_df["chamber_temp_c"].mean()
temp_std = sensor_df["chamber_temp_c"].std(ddof=1)
pressure_mean = sensor_df["chamber_pressure_pa"].mean()
pressure_std = sensor_df["chamber_pressure_pa"].std(ddof=1)

temp_alarm = (
    sensor_df["chamber_temp_c"] > temp_mean + 3 * temp_std
)
pressure_alarm = (
    sensor_df["chamber_pressure_pa"] > pressure_mean + 3 * pressure_std
)
vibration_alarm = sensor_df["vibration_g"] >= 0.15
particle_alarm = sensor_df["particle_count"] >= 10

sensor_df["risk_score"] = (
    temp_alarm.astype(int) * 40
    + pressure_alarm.astype(int) * 30
    + vibration_alarm.astype(int) * 20
    + particle_alarm.astype(int) * 10
)
sensor_df["high_risk"] = sensor_df["risk_score"] >= 50

recent_high_count = (
    sensor_df["high_risk"]
    .astype(int)
    .rolling(window=5, min_periods=1)
    .sum()
)
sensor_df["persistent_alarm"] = recent_high_count >= 3

alarm_start = (
    sensor_df["persistent_alarm"]
    & ~sensor_df["persistent_alarm"].shift(1, fill_value=False)
)

start_df = sensor_df.loc[
    alarm_start,
    ["timestamp", "lot_id", "risk_score"],
]

print("지속 경보 시작 수:", len(start_df))
print(start_df)
start_df.to_csv(
    OUTPUT_DIR / "ex058_persistent_alarm_starts.csv",
    index=False,
    encoding="utf-8-sig",
)
