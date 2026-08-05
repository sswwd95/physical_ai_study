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

allowed_lots = {"LOT-A", "LOT-B", "LOT-C"}
allowed_states = {"stabilize", "process", "purge"}

invalid_lot = ~quality_df["lot_id"].isin(allowed_lots)
invalid_state = ~quality_df["process_state"].isin(allowed_states)
quality_df["invalid_category"] = invalid_lot | invalid_state

problem_df = quality_df.loc[
    quality_df["invalid_category"],
    ["timestamp", "lot_id", "process_state", "invalid_category"],
]

print("잘못된 범주 행 수:", len(problem_df))
print(problem_df)
problem_df.to_csv(
    OUTPUT_DIR / "ex032_invalid_categories.csv",
    index=False,
    encoding="utf-8-sig",
)
