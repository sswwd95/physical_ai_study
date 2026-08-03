"""
반도체 Physical AI 하네스 엔지니어링 실습 021~025
Windows 10 / Anaconda / Pandas
결측값 탐지와 처리 품질 비교
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_missing.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "sensor_log_linear_interpolation.csv"
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

# 1. 원본 결측 위치를 저장한다.
original_missing_mask = df[sensor_columns].isna()

# 2. 내부 결측값을 선형 보간한다.
interpolated = df.copy()
interpolated[sensor_columns] = (
    interpolated[sensor_columns]
    .interpolate(
        method="linear",
        limit_area="inside",
    )
)

# 3. 시작과 끝에 남은 결측값은 전·후방 값으로 채운다.
interpolated[sensor_columns] = (
    interpolated[sensor_columns]
    .ffill()
    .bfill()
)

# 4. 센서별 보간 여부를 기록한다.
for sensor in sensor_columns:
    interpolated[f"{sensor}_was_interpolated"] = (
        original_missing_mask[sensor]
        & interpolated[sensor].notna()
    )

# 5. 결과를 저장한다.
interpolated.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

remaining_missing = int(
    interpolated[sensor_columns]
    .isna()
    .sum()
    .sum()
)

print("처리 후 전체 결측 개수:", remaining_missing)
print(
    "주의: 긴 결측 구간의 선형 보간은 "
    "실제 공정 변화를 과도하게 단순화할 수 있습니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
