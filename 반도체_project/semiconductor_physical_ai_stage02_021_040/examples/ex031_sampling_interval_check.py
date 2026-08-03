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

quality_df["interval_seconds"] = (
    quality_df["timestamp"].diff().dt.total_seconds()
)

def classify_gap(interval):
    if pd.isna(interval) or interval == 1:
        return "normal"
    if interval <= 0:
        return "duplicate_or_reverse"
    return "missing_or_delay"

quality_df["gap_type"] = quality_df["interval_seconds"].apply(classify_gap)
gap_df = quality_df.loc[quality_df["gap_type"] != "normal"]

print(gap_df[["timestamp", "interval_seconds", "gap_type"]])
gap_df.to_csv(
    OUTPUT_DIR / "ex031_sampling_interval_gaps.csv",
    index=False,
    encoding="utf-8-sig",
)
