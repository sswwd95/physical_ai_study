"""
반도체 Physical AI 하네스 엔지니어링 실습 026~030
Windows 10 / Anaconda / Pandas / SciPy
이상값 탐지와 보정 품질 비교
"""

from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_outliers.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "sensor_log_hampel_filtered.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

window_size = 15
n_sigma = 3.0

filtered = df.copy()

for sensor in sensor_columns:
    # 1. 이동 중앙값을 계산한다.
    rolling_median = (
        df[sensor]
        .rolling(
            window=window_size,
            center=True,
            min_periods=5,
        )
        .median()
    )

    # 2. 이동 중앙절대편차(MAD)를 계산한다.
    absolute_deviation = (
        df[sensor] - rolling_median
    ).abs()

    rolling_mad = (
        absolute_deviation
        .rolling(
            window=window_size,
            center=True,
            min_periods=5,
        )
        .median()
    )

    # 3. MAD를 정규분포 표준편차 규모로 환산한다.
    robust_sigma = 1.4826 * rolling_mad

    # 4. 임계값을 넘는 값을 Hampel 이상값으로 판단한다.
    threshold = n_sigma * robust_sigma

    is_outlier = (
        absolute_deviation > threshold
    ) & rolling_median.notna()

    # 5. 이상값은 이동 중앙값으로 대체한다.
    filtered.loc[is_outlier, sensor] = (
        rolling_median[is_outlier]
    )

    # 6. 원래 값이 대체되었는지 표시한다.
    filtered[f"{sensor}_hampel_outlier"] = (
        is_outlier
    )

# 7. 결과를 저장한다.
filtered.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

flag_columns = [
    f"{sensor}_hampel_outlier"
    for sensor in sensor_columns
]

print("[센서별 Hampel 이상값 개수]")
print(filtered[flag_columns].sum())
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
