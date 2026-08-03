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
    / "missing_value_summary.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 분석 대상 센서 열을 정의한다.
sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 2. 센서별 결측값 개수를 계산한다.
missing_count = df[sensor_columns].isna().sum()

# 3. 센서별 결측률을 백분율로 계산한다.
missing_rate = (
    missing_count / len(df) * 100.0
)

# 4. 결과를 표 형태로 만든다.
summary = pd.DataFrame(
    {
        "sensor": sensor_columns,
        "missing_count": [
            int(missing_count[column])
            for column in sensor_columns
        ],
        "missing_rate_percent": [
            float(missing_rate[column])
            for column in sensor_columns
        ],
    }
)

# 5. 결측률이 높은 순서로 정렬한다.
summary = summary.sort_values(
    "missing_rate_percent",
    ascending=False,
).reset_index(drop=True)

# 6. 결측값이 하나라도 있는 행의 개수를 계산한다.
rows_with_missing = int(
    df[sensor_columns].isna().any(axis=1).sum()
)

# 7. 결과를 CSV로 저장한다.
summary.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[센서별 결측 요약]")
print(summary.round(4))
print()
print("전체 행:", len(df))
print("결측 포함 행:", rows_with_missing)
print(
    "결측 포함 행 비율(%):",
    round(rows_with_missing / len(df) * 100.0, 4),
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
