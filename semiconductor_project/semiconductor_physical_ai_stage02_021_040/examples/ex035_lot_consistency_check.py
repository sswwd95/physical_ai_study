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

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

lot_summary = (
    sensor_df.groupby("lot_id")
    .agg(
        row_count=("timestamp", "size"),
        first_timestamp=("timestamp", "min"),
        last_timestamp=("timestamp", "max"),
        state_count=("process_state", "nunique"),
        states=("process_state", lambda x: ",".join(sorted(x.unique()))),
    )
    .reset_index()
)

lot_summary["lot_count_error"] = lot_summary["row_count"] != 100

print(lot_summary)
lot_summary.to_csv(
    OUTPUT_DIR / "ex035_lot_consistency.csv",
    index=False,
    encoding="utf-8-sig",
)
