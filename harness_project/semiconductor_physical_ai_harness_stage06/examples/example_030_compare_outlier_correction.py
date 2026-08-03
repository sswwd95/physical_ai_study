"""
반도체 Physical AI 하네스 엔지니어링 실습 026~030
Windows 10 / Anaconda / Pandas / SciPy
이상값 탐지와 보정 품질 비교
"""

from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

COMPLETE_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_complete.csv"
)
OUTLIER_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_outliers.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "outlier_correction_quality.csv"
)

complete_df = pd.read_csv(
    COMPLETE_PATH,
    parse_dates=["timestamp"],
)

outlier_df = pd.read_csv(
    OUTLIER_PATH,
    parse_dates=["timestamp"],
)

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 원본과 다른 위치를 실제 이상값 위치로 사용한다.
true_outlier_mask = pd.DataFrame(
    {
        sensor: ~np.isclose(
            complete_df[sensor],
            outlier_df[sensor],
        )
        for sensor in sensor_columns
    }
)

# 2. 중앙값 대체 결과를 만든다.
median_corrected = outlier_df[sensor_columns].copy()

for sensor in sensor_columns:
    median_value = float(
        outlier_df[sensor].median()
    )
    median_corrected.loc[
        true_outlier_mask[sensor],
        sensor,
    ] = median_value

# 3. 선형 보간 결과를 만든다.
linear_corrected = outlier_df[sensor_columns].copy()

for sensor in sensor_columns:
    linear_corrected.loc[
        true_outlier_mask[sensor],
        sensor,
    ] = np.nan

linear_corrected = (
    linear_corrected
    .interpolate(
        method="linear",
        limit_area="inside",
    )
    .ffill()
    .bfill()
)

# 4. Hampel 방식 결과를 직접 계산한다.
hampel_corrected = outlier_df[sensor_columns].copy()

for sensor in sensor_columns:
    series = outlier_df[sensor]

    rolling_median = series.rolling(
        window=15,
        center=True,
        min_periods=5,
    ).median()

    absolute_deviation = (
        series - rolling_median
    ).abs()

    rolling_mad = absolute_deviation.rolling(
        window=15,
        center=True,
        min_periods=5,
    ).median()

    threshold = 3.0 * 1.4826 * rolling_mad

    detected = (
        absolute_deviation > threshold
    ) & rolling_median.notna()

    hampel_corrected.loc[
        detected,
        sensor,
    ] = rolling_median[detected]

methods = {
    "median_replace": median_corrected,
    "linear_interpolation": linear_corrected,
    "hampel_filter": hampel_corrected,
}

rows = []

# 5. 실제 이상값이 주입된 위치에서만 복원 오차를 계산한다.
for method_name, corrected_df in methods.items():
    for sensor in sensor_columns:
        mask = true_outlier_mask[sensor]

        if int(mask.sum()) == 0:
            continue

        actual = complete_df.loc[
            mask,
            sensor,
        ].to_numpy()

        predicted = corrected_df.loc[
            mask,
            sensor,
        ].to_numpy()

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

        rows.append(
            {
                "method": method_name,
                "sensor": sensor,
                "outlier_points": int(mask.sum()),
                "mae": mae,
                "rmse": rmse,
            }
        )

result = pd.DataFrame(rows)

# 6. 센서별로 RMSE가 가장 작은 방법을 표시한다.
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

print("[이상값 보정 품질 비교]")
print(result.round(5))
print()
print(
    "해석: MAE와 RMSE가 작을수록 "
    "원래 센서값을 더 가깝게 복원했습니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
