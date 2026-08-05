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

missing_profile = pd.DataFrame({
    "column": quality_df.columns,
    "missing_count": quality_df.isna().sum().values,
    "missing_ratio": quality_df.isna().mean().values,
}).sort_values("missing_ratio", ascending=False)

print(missing_profile)
missing_profile.to_csv(
    OUTPUT_DIR / "ex026_missing_profile.csv",
    index=False,
    encoding="utf-8-sig",
)
