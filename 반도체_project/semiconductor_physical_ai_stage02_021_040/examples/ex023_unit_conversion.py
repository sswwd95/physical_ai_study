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

sensor_df["chamber_temp_k"] = sensor_df["chamber_temp_c"] + 273.15
sensor_df["chamber_pressure_kpa"] = sensor_df["chamber_pressure_pa"] / 1000.0
sensor_df["vibration_m_s2"] = sensor_df["vibration_g"] * 9.80665

result_columns = [
    "timestamp",
    "chamber_temp_c",
    "chamber_temp_k",
    "chamber_pressure_pa",
    "chamber_pressure_kpa",
    "vibration_g",
    "vibration_m_s2",
]
result_df = sensor_df[result_columns]

print(result_df.head().round(5))
result_df.to_csv(
    OUTPUT_DIR / "ex023_unit_conversion.csv",
    index=False,
    encoding="utf-8-sig",
)
