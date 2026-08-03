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

quality_df = pd.read_csv(QUALITY_FILE)

full_duplicate_mask = quality_df.duplicated(keep=False)
key_duplicate_mask = quality_df.duplicated(
    subset=["timestamp", "lot_id"],
    keep=False,
)

full_duplicates = quality_df.loc[full_duplicate_mask]
key_duplicates = quality_df.loc[key_duplicate_mask].sort_values(
    ["timestamp", "lot_id"]
)

print("완전 중복 행 수:", len(full_duplicates))
print("복합키 중복 행 수:", len(key_duplicates))
print(key_duplicates[["timestamp", "lot_id", "process_state"]])

key_duplicates.to_csv(
    OUTPUT_DIR / "ex028_duplicate_keys.csv",
    index=False,
    encoding="utf-8-sig",
)
