from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

purge_high_rf = (
    (sensor_df["process_state"] == "purge")
    & (sensor_df["rf_power_w"] >= 900)
)
stabilize_high_vibration = (
    (sensor_df["process_state"] == "stabilize")
    & (sensor_df["vibration_g"] >= 0.12)
)

sensor_df["contextual_anomaly"] = (
    purge_high_rf | stabilize_high_vibration
)

print("purge 고전력:", int(purge_high_rf.sum()))
print("stabilize 고진동:", int(stabilize_high_vibration.sum()))

sensor_df.loc[sensor_df["contextual_anomaly"]].to_csv(
    OUTPUT_DIR / "ex084_contextual_anomalies.csv",
    index=False,
    encoding="utf-8-sig",
)
