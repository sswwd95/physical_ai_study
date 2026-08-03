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
    (sensor_df["chamber_temp_c"] > temp_mean + 3 * temp_std)
    | (sensor_df["chamber_temp_c"] < temp_mean - 3 * temp_std)
)
pressure_alarm = (
    (sensor_df["chamber_pressure_pa"] > pressure_mean + 3 * pressure_std)
    | (sensor_df["chamber_pressure_pa"] < pressure_mean - 3 * pressure_std)
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

risk_df = sensor_df.loc[
    sensor_df["high_risk"],
    [
        "timestamp",
        "lot_id",
        "chamber_temp_c",
        "chamber_pressure_pa",
        "vibration_g",
        "particle_count",
        "risk_score",
    ],
]

print("고위험 행 수:", len(risk_df))
print(risk_df.head(20).round(3))
risk_df.to_csv(
    OUTPUT_DIR / "ex057_high_risk_rows.csv",
    index=False,
    encoding="utf-8-sig",
)
