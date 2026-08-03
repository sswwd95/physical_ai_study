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

for column in ["chamber_temp_c", "chamber_pressure_pa"]:
    lower = sensor_df[column].quantile(0.01)
    upper = sensor_df[column].quantile(0.99)
    new_column = f"{column}_winsorized"

    sensor_df[new_column] = sensor_df[column].clip(lower=lower, upper=upper)
    changed_count = int((sensor_df[column] != sensor_df[new_column]).sum())

    print(column)
    print("변경 행 수:", changed_count)
    print(
        "원본 범위:",
        round(sensor_df[column].min(), 3),
        "~",
        round(sensor_df[column].max(), 3),
    )
    print(
        "보정 범위:",
        round(sensor_df[new_column].min(), 3),
        "~",
        round(sensor_df[new_column].max(), 3),
    )

sensor_df.to_csv(
    OUTPUT_DIR / "ex034_winsorized_sensors.csv",
    index=False,
    encoding="utf-8-sig",
)
