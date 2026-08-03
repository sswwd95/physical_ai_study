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

print("데이터 크기:", sensor_df.shape)
print("이상 건수:", int(sensor_df["true_anomaly"].sum()))
print("이상 비율:", round(sensor_df["true_anomaly"].mean(), 4))

group_summary = (
    sensor_df.groupby("true_anomaly")[
        [
            "chamber_temp_c",
            "chamber_pressure_pa",
            "rf_power_w",
            "vibration_g",
            "particle_count",
        ]
    ]
    .mean()
)

print(group_summary.round(3))
group_summary.to_csv(
    OUTPUT_DIR / "ex081_anomaly_group_summary.csv",
    encoding="utf-8-sig",
)
