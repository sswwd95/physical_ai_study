"""
반도체 Physical AI 하네스 엔지니어링 실습 011~015
Windows 10 / Anaconda / Pandas / PyMC 연계 준비
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"

# 1. 센서 CSV를 읽으면서 timestamp 열을 날짜·시간 형식으로 변환한다.
df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 2. 분석에 필요한 필수 열을 정의한다.
required_columns = [
    "timestamp",
    "lot_id",
    "recipe_id",
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 3. 필수 열 누락 여부를 검사한다.
missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(f"필수 열이 누락되었습니다: {missing_columns}")

# 4. 데이터의 기본 구조와 시간 범위를 확인한다.
print("[데이터 크기]", df.shape)
print("[열 목록]", list(df.columns))
print("[시작 시각]", df["timestamp"].min())
print("[종료 시각]", df["timestamp"].max())
print("[Lot 목록]", sorted(df["lot_id"].dropna().unique()))
print("[Recipe 목록]", sorted(df["recipe_id"].dropna().unique()))

# 5. 센서 열의 자료형을 확인한다.
sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

print("\n[센서 자료형]")
print(df[sensor_columns].dtypes)

# 6. 앞부분 5행을 출력해 실제 데이터 형태를 점검한다.
print("\n[처음 5행]")
print(df.head())
