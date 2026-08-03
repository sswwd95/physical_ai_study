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

required_columns = [
    "timestamp",
    "lot_id",
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
    "particle_count",
    "process_state",
]

missing_columns = [c for c in required_columns if c not in sensor_df.columns]
unexpected_columns = [c for c in sensor_df.columns if c not in required_columns]

print("현재 컬럼 순서:", sensor_df.columns.tolist())
print("누락 컬럼:", missing_columns)
print("예상하지 않은 컬럼:", unexpected_columns)
print("스키마 검사:", "PASS" if not missing_columns else "FAIL")
