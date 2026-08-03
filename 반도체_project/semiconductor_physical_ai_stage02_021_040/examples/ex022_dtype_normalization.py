from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "기본 데이터가 없습니다. 프로젝트 루트에서 "
        "python generate_base_data.py를 먼저 실행하세요."
    )

sensor_df = pd.read_csv(DATA_FILE)

print("변환 전 자료형:")
print(sensor_df.dtypes)

sensor_df["timestamp"] = pd.to_datetime(sensor_df["timestamp"], errors="coerce")

float_columns = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
]
for column in float_columns:
    sensor_df[column] = pd.to_numeric(sensor_df[column], errors="coerce").astype(float)

sensor_df["particle_count"] = (
    pd.to_numeric(sensor_df["particle_count"], errors="coerce")
    .round()
    .astype("Int64")
)
sensor_df["lot_id"] = sensor_df["lot_id"].astype("category")
sensor_df["process_state"] = sensor_df["process_state"].astype("category")

print("\n변환 후 자료형:")
print(sensor_df.dtypes)

sensor_df.to_csv(
    OUTPUT_DIR / "ex022_normalized_dtypes.csv",
    index=False,
    encoding="utf-8-sig",
)
