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

quality_df["has_missing"] = quality_df.isna().any(axis=1)
quality_df["invalid_state"] = ~quality_df["process_state"].isin(
    ["stabilize", "process", "purge"]
)
quality_df["range_violation"] = (
    ~quality_df["chamber_temp_c"].between(65, 80)
    | ~quality_df["chamber_pressure_pa"].between(15, 22)
    | ~quality_df["rf_power_w"].between(780, 920)
    | ~quality_df["gas_flow_sccm"].between(105, 135)
    | ~quality_df["vibration_g"].between(0, 0.25)
)
quality_df["is_duplicate"] = quality_df.duplicated(keep=False)

penalty_columns = [
    "has_missing",
    "invalid_state",
    "range_violation",
    "is_duplicate",
]
quality_df["quality_score"] = (
    100 - quality_df[penalty_columns].sum(axis=1) * 25
)

quality_df["quality_grade"] = pd.cut(
    quality_df["quality_score"],
    bins=[-1, 49, 74, 89, 100],
    labels=["D", "C", "B", "A"],
)

print(quality_df["quality_grade"].value_counts().sort_index())
quality_df.to_csv(
    OUTPUT_DIR / "ex038_quality_score.csv",
    index=False,
    encoding="utf-8-sig",
)
