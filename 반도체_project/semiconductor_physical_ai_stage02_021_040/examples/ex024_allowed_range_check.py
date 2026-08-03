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

allowed_ranges = {
    "chamber_temp_c": (65.0, 80.0),
    "chamber_pressure_pa": (15.0, 22.0),
    "rf_power_w": (780.0, 920.0),
    "gas_flow_sccm": (105.0, 135.0),
    "vibration_g": (0.0, 0.25),
    "particle_count": (0, 40),
}

violation_columns = []
for column, (lower, upper) in allowed_ranges.items():
    flag_column = f"{column}_range_violation"
    sensor_df[flag_column] = ~sensor_df[column].between(lower, upper)
    violation_columns.append(flag_column)
    print(column, "위반 건수:", int(sensor_df[flag_column].sum()))

sensor_df["any_range_violation"] = sensor_df[violation_columns].any(axis=1)

print("전체 범위 위반 행:", int(sensor_df["any_range_violation"].sum()))
sensor_df.to_csv(
    OUTPUT_DIR / "ex024_allowed_range_check.csv",
    index=False,
    encoding="utf-8-sig",
)
