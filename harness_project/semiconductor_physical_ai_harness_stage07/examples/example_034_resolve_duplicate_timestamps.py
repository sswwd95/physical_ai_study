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
    / "sensor_log_deduplicated.csv"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "duplicate_timestamp_report.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 중복 시각에 포함된 모든 행을 찾는다.
duplicate_mask = df.duplicated(
    subset=["timestamp"],
    keep=False,
)

duplicate_rows = df.loc[
    duplicate_mask
].sort_values("timestamp")

duplicate_rows.to_csv(
    REPORT_PATH,
    index=False,
    encoding="utf-8-sig",
)

# 2. 중복 시각은 센서 평균으로 통합한다.
sensor_aggregations = {
    sensor: "mean"
    for sensor in sensor_columns
}

aggregations = {
    "lot_id": "first",
    "recipe_id": "first",
    **sensor_aggregations,
}

deduplicated = (
    df.groupby(
        "timestamp",
        as_index=False,
    )
    .agg(aggregations)
    .sort_values("timestamp")
    .reset_index(drop=True)
)

# 3. 중복 시각이 모두 제거되었는지 검사한다.
remaining_duplicates = int(
    deduplicated["timestamp"]
    .duplicated()
    .sum()
)

if remaining_duplicates != 0:
    raise RuntimeError(
        "중복 시각 제거에 실패했습니다."
    )

# 4. 정리된 데이터를 저장한다.
deduplicated.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("원본 행 수:", len(df))
print("중복 통합 후 행 수:", len(deduplicated))
print("중복 관련 원본 행 수:", len(duplicate_rows))
print(f"[완료] 정리 데이터: {OUTPUT_PATH}")
print(f"[완료] 중복 리포트: {REPORT_PATH}")
