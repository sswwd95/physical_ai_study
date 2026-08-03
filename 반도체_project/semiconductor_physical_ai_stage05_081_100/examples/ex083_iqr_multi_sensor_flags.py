from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE)

features = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
    "particle_count",
]

flags = []
for column in features:
    q1 = sensor_df[column].quantile(0.25)
    q3 = sensor_df[column].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    flag = f"{column}_iqr_anomaly"
    sensor_df[flag] = ~sensor_df[column].between(lower, upper)
    flags.append(flag)

sensor_df["anomaly_sensor_count"] = sensor_df[flags].sum(axis=1)
sensor_df["multi_iqr_anomaly"] = (
    sensor_df["anomaly_sensor_count"] >= 2
)

print(
    "다중 IQR 이상 행:",
    int(sensor_df["multi_iqr_anomaly"].sum()),
)
