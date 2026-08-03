"""
반도체 Physical AI 하네스 엔지니어링 실습
Windows 10 / Anaconda / PyMC
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
csv_path = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"

# 1. 하네스가 기대하는 필수 열과 데이터 범위를 정의한다.
REQUIRED_COLUMNS = {
    "timestamp": None,
    "temperature_c": (0.0, 150.0),
    "pressure_kpa": (80.0, 130.0),
    "gas_flow_sccm": (0.0, 1000.0),
    "vibration_rms": (0.0, 20.0),
    "motor_current_a": (0.0, 50.0),
}

# 2. 센서 로그를 읽고 시간 열을 datetime 형식으로 변환한다.
df = pd.read_csv(csv_path)
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# 3. 필수 열 누락 여부를 검사한다.
missing_columns = [
    column for column in REQUIRED_COLUMNS
    if column not in df.columns
]

if missing_columns:
    raise ValueError(f"필수 열 누락: {missing_columns}")

# 4. 결측값과 허용 범위를 검사한다.
issues = []

for column, valid_range in REQUIRED_COLUMNS.items():
    missing_count = int(df[column].isna().sum())
    if missing_count > 0:
        issues.append(f"{column}: 결측값 {missing_count}개")

    if valid_range is not None:
        low, high = valid_range
        invalid_count = int((~df[column].between(low, high)).sum())
        if invalid_count > 0:
            issues.append(
                f"{column}: 범위 밖 데이터 {invalid_count}개 "
                f"(허용 {low}~{high})"
            )

# 5. 시간 순서가 증가하는지도 검사한다.
if not df["timestamp"].is_monotonic_increasing:
    issues.append("timestamp: 시간 순서가 오름차순이 아님")

# 6. 최종 검사 결과를 출력한다.
if issues:
    print("[검사 실패]")
    for issue in issues:
        print("-", issue)
else:
    print("[검사 통과] 센서 데이터 스키마와 기본 품질이 정상입니다.")
