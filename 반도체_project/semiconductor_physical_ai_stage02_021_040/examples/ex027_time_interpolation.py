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

QUALITY_FILE = ROOT / "data" / "sensor_data_with_quality_errors.csv"
if not QUALITY_FILE.exists():
    raise FileNotFoundError("실습 025를 먼저 실행하세요.")

quality_df = pd.read_csv(QUALITY_FILE, parse_dates=["timestamp"])
quality_df = quality_df.sort_values("timestamp").reset_index(drop=True)

target_columns = ["chamber_pressure_pa", "rf_power_w"]
before_missing = quality_df[target_columns].isna().sum()

quality_df = quality_df.set_index("timestamp")
quality_df[target_columns] = quality_df[target_columns].interpolate(
    method="time",
    limit_direction="both",
)
quality_df = quality_df.reset_index()

after_missing = quality_df[target_columns].isna().sum()

print("보간 전:\n", before_missing)
print("\n보간 후:\n", after_missing)
quality_df.to_csv(
    OUTPUT_DIR / "ex027_time_interpolated.csv",
    index=False,
    encoding="utf-8-sig",
)
