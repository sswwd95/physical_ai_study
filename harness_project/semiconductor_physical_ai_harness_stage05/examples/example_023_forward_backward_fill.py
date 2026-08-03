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
    / "sensor_log_ffill_bfill.csv"
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

# 1. 처리 전 결측 개수를 기록한다.
before_missing = df[sensor_columns].isna().sum()

# 2. 먼저 직전 정상값으로 전방 채우기를 수행한다.
filled = df.copy()
filled[sensor_columns] = (
    filled[sensor_columns]
    .ffill()
)

# 3. 시작 부분에 남은 결측값은 다음 정상값으로 후방 채운다.
filled[sensor_columns] = (
    filled[sensor_columns]
    .bfill()
)

# 4. 처리 후 결측 개수를 계산한다.
after_missing = filled[sensor_columns].isna().sum()

# 5. 어떤 값이 대체되었는지 센서별 표시 열을 만든다.
for sensor in sensor_columns:
    filled[f"{sensor}_was_imputed"] = (
        df[sensor].isna()
        & filled[sensor].notna()
    )

# 6. 결과를 저장한다.
filled.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

comparison = pd.DataFrame(
    {
        "before_missing": before_missing,
        "after_missing": after_missing,
    }
)

print("[전·후방 채우기 결과]")
print(comparison)
print()
print(
    "주의: 전방 채우기는 센서값이 급변하는 공정에서 "
    "실제 변화를 숨길 수 있습니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
