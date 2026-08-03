"""
반도체 Physical AI 하네스 엔지니어링 실습 036~040
Windows 10 / Anaconda / Pandas / SciPy
센서 노이즈 분석과 필터링
"""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEAN_PATH = PROJECT_ROOT / "data" / "sensor_signal_clean.csv"
NOISY_PATH = PROJECT_ROOT / "data" / "sensor_signal_noisy.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "filter_performance_comparison.csv"

clean_df = pd.read_csv(CLEAN_PATH, parse_dates=["timestamp"])
noisy_df = pd.read_csv(NOISY_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 세 가지 필터 결과를 만든다.
moving_average = noisy_df[sensor_columns].rolling(
    window=11,
    center=True,
    min_periods=1,
).mean()

exponential = noisy_df[sensor_columns].ewm(
    alpha=0.20,
    adjust=False,
).mean()

savgol = pd.DataFrame(
    {
        sensor: savgol_filter(
            noisy_df[sensor].to_numpy(),
            window_length=15,
            polyorder=2,
            mode="interp",
        )
        for sensor in sensor_columns
    }
)

methods = {
    "moving_average": moving_average,
    "exponential_smoothing": exponential,
    "savgol_filter": savgol,
}

rows = []

# 2. 깨끗한 기준 신호와 각 필터 결과의 오차를 계산한다.
for method_name, filtered_df in methods.items():
    for sensor in sensor_columns:
        actual = clean_df[sensor].to_numpy()
        predicted = filtered_df[sensor].to_numpy()

        mae = float(
            np.mean(np.abs(actual - predicted))
        )

        rmse = float(
            np.sqrt(
                np.mean(
                    (actual - predicted) ** 2
                )
            )
        )

        # 3. 1차 차분의 표준편차로 잔여 거칠기를 계산한다.
        roughness = float(
            np.std(
                np.diff(predicted),
                ddof=1,
            )
        )

        rows.append(
            {
                "method": method_name,
                "sensor": sensor,
                "mae": mae,
                "rmse": rmse,
                "roughness": roughness,
            }
        )

result = pd.DataFrame(rows)
result["best_rmse_for_sensor"] = False

for sensor in result["sensor"].unique():
    sensor_mask = result["sensor"] == sensor
    best_index = (
        result.loc[sensor_mask, "rmse"]
        .idxmin()
    )
    result.loc[
        best_index,
        "best_rmse_for_sensor",
    ] = True

result = result.sort_values(
    ["sensor", "rmse"]
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[필터 성능 비교]")
print(result.round(6))
print()
print(
    "RMSE는 기준 신호 복원 정확도, roughness는 "
    "필터 결과의 잔여 흔들림 정도를 나타냅니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
