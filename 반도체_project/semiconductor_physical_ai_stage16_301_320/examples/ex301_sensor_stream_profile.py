from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/digital_twin_sensor_stream.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

print("데이터 크기:", sensor_df.shape)
print("\n공정 단계:")
print(sensor_df["process_phase"].value_counts())
print("\n센서 결측값:")
print(sensor_df.isna().sum())
print("\n센서 기본 통계:")
print(
    sensor_df[
        [
            "temp_sensor_a_c",
            "temp_sensor_b_c",
            "pressure_sensor_a_pa",
            "pressure_sensor_b_pa",
            "rf_sensor_w",
            "gas_sensor_sccm",
        ]
    ].describe().round(3)
)
