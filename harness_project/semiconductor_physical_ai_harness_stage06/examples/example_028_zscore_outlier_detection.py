"""
반도체 Physical AI 하네스 엔지니어링 실습 026~030
Windows 10 / Anaconda / Pandas / SciPy
이상값 탐지와 보정 품질 비교
"""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import zscore

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_outliers.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "zscore_outlier_rows.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 센서별 Z-score를 계산한다.
zscore_df = pd.DataFrame(index=df.index)

for sensor in sensor_columns:
    zscore_df[f"{sensor}_zscore"] = zscore(
        df[sensor],
        nan_policy="omit",
    )

# 2. 절대 Z-score가 3 이상인 값을 이상값 후보로 표시한다.
flag_df = zscore_df.abs() >= 3.0

# 3. 하나 이상의 센서가 이상이면 해당 행을 추출한다.
row_mask = flag_df.any(axis=1)

result = df.loc[
    row_mask,
    ["timestamp", "lot_id", "recipe_id"] + sensor_columns,
].copy()

# 4. Z-score와 이상 센서 목록을 추가한다.
for column in zscore_df.columns:
    result[column] = zscore_df.loc[row_mask, column]

def collect_outlier_sensors(index):
    sensors = []

    for sensor in sensor_columns:
        if flag_df.loc[index, f"{sensor}_zscore"]:
            sensors.append(sensor)

    return ",".join(sensors)

result["outlier_sensors"] = [
    collect_outlier_sensors(index)
    for index in result.index
]

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[Z-score 이상값 행]")
print(result.round(4))
print()
print("이상 행 수:", len(result))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
