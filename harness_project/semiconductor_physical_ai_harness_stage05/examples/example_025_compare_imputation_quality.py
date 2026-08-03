"""
반도체 Physical AI 하네스 엔지니어링 실습 021~025
Windows 10 / Anaconda / Pandas
결측값 탐지와 처리 품질 비교
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
MISSING_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_missing.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "imputation_quality_comparison.csv"
)

complete_df = pd.read_csv(
    COMPLETE_PATH,
    parse_dates=["timestamp"],
)

missing_df = pd.read_csv(
    MISSING_PATH,
    parse_dates=["timestamp"],
)

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 결측 위치 마스크를 만든다.
missing_mask = missing_df[sensor_columns].isna()

# 2. 비교할 세 가지 처리 방법을 생성한다.
ffill_bfill = (
    missing_df[sensor_columns]
    .ffill()
    .bfill()
)

linear = (
    missing_df[sensor_columns]
    .interpolate(
        method="linear",
        limit_area="inside",
    )
    .ffill()
    .bfill()
)

median = missing_df[sensor_columns].copy()

for sensor in sensor_columns:
    median[sensor] = median[sensor].fillna(
        median[sensor].median()
    )

methods = {
    "ffill_bfill": ffill_bfill,
    "linear_interpolation": linear,
    "median_fill": median,
}

rows = []

# 3. 원래 결측이었던 위치에서만 복원 오차를 계산한다.
for method_name, imputed_df in methods.items():
    for sensor in sensor_columns:
        mask = missing_mask[sensor]

        actual = complete_df.loc[mask, sensor].to_numpy()
        predicted = imputed_df.loc[mask, sensor].to_numpy()

        if len(actual) == 0:
            continue

        mae = float(
            np.mean(np.abs(actual - predicted))
        )
        rmse = float(
            np.sqrt(np.mean((actual - predicted) ** 2))
        )

        rows.append(
            {
                "method": method_name,
                "sensor": sensor,
                "missing_points": int(mask.sum()),
                "mae": mae,
                "rmse": rmse,
            }
        )

# 4. 센서별·방법별 결과 표를 만든다.
result = pd.DataFrame(rows)

# 5. 센서마다 RMSE가 가장 작은 방법을 표시한다.
result["best_rmse_for_sensor"] = False

for sensor in result["sensor"].unique():
    sensor_rows = result["sensor"] == sensor
    best_index = (
        result.loc[sensor_rows, "rmse"]
        .idxmin()
    )
    result.loc[
        best_index,
        "best_rmse_for_sensor",
    ] = True

# 6. 결과를 저장한다.
result = result.sort_values(
    ["sensor", "rmse"]
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[결측 처리 품질 비교]")
print(result.round(5))
print()
print(
    "해석: MAE와 RMSE가 작을수록 원래 센서값을 "
    "더 가깝게 복원한 것입니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
