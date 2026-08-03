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
sensor_df = sensor_df.sort_values("timestamp").reset_index(drop=True)

allowed_transitions = {
    ("stabilize", "stabilize"),
    ("stabilize", "process"),
    ("process", "process"),
    ("process", "purge"),
    ("purge", "purge"),
    ("purge", "stabilize"),
}

sensor_df["next_state"] = sensor_df["process_state"].shift(-1)
sensor_df["transition_allowed"] = sensor_df.apply(
    lambda row: True
    if pd.isna(row["next_state"])
    else (row["process_state"], row["next_state"]) in allowed_transitions,
    axis=1,
)

invalid_df = sensor_df.loc[
    ~sensor_df["transition_allowed"],
    ["timestamp", "process_state", "next_state"],
]

print("잘못된 상태 전이 수:", len(invalid_df))
print(invalid_df)
invalid_df.to_csv(
    OUTPUT_DIR / "ex036_invalid_state_transitions.csv",
    index=False,
    encoding="utf-8-sig",
)
