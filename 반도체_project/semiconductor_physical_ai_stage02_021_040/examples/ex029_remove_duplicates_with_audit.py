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

duplicate_mask = quality_df.duplicated(keep="first")
duplicate_audit = quality_df.loc[duplicate_mask].copy()
clean_df = quality_df.loc[~duplicate_mask].copy().reset_index(drop=True)

print("처리 전:", len(quality_df))
print("제거 수:", int(duplicate_mask.sum()))
print("처리 후:", len(clean_df))

duplicate_audit.to_csv(
    OUTPUT_DIR / "ex029_duplicate_audit.csv",
    index=False,
    encoding="utf-8-sig",
)
clean_df.to_csv(
    OUTPUT_DIR / "ex029_cleaned_no_duplicates.csv",
    index=False,
    encoding="utf-8-sig",
)
