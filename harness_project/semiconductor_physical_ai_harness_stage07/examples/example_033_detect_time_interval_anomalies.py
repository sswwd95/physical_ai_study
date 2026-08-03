"""
반도체 Physical AI 하네스 엔지니어링 실습 031~035
Windows 10 / Anaconda / Pandas
단위, 시간축, 중복, 드리프트 데이터 품질
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_timing_issues.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "time_interval_anomalies.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 시간 오름차순으로 정렬한다.
df = df.sort_values("timestamp").reset_index(drop=True)

# 2. 현재 시각과 이전 시각의 차이를 초 단위로 계산한다.
df["interval_sec"] = (
    df["timestamp"]
    .diff()
    .dt.total_seconds()
)

# 3. 기대 샘플링 간격을 1초로 정의한다.
expected_interval_sec = 1.0
tolerance_sec = 0.01

# 4. 중복 시각과 긴 간격을 구분한다.
df["duplicate_timestamp"] = (
    df["interval_sec"] == 0.0
)

df["gap_detected"] = (
    df["interval_sec"]
    > expected_interval_sec + tolerance_sec
)

df["interval_anomaly"] = (
    df["duplicate_timestamp"]
    | df["gap_detected"]
)

# 5. 이상 시간 행만 추출한다.
result = df.loc[
    df["interval_anomaly"],
    [
        "timestamp",
        "lot_id",
        "recipe_id",
        "interval_sec",
        "duplicate_timestamp",
        "gap_detected",
    ],
].copy()

# 6. 누락된 샘플 수를 근사 계산한다.
result["estimated_missing_samples"] = (
    result["interval_sec"]
    .sub(expected_interval_sec)
    .clip(lower=0)
    .round()
    .astype(int)
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[시간 간격 이상]")
print(result)
print()
print("이상 행 수:", len(result))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
