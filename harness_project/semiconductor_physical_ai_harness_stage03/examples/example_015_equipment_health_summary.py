"""
반도체 Physical AI 하네스 엔지니어링 실습 011~015
Windows 10 / Anaconda / Pandas / PyMC 연계 준비
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "equipment_health_summary.csv"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "equipment_health_summary.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 교육용 설비 상태 기준을 정의한다.
limits = {
    "temperature_c": (62.0, 69.0),
    "pressure_kpa": (99.5, 103.0),
    "gas_flow_sccm": (485.0, 515.0),
    "vibration_rms": (0.0, 2.5),
    "motor_current_a": (0.0, 9.0),
}

# 2. 센서별 범위 이탈 여부를 만든다.
alarm_columns = []

for sensor, (low, high) in limits.items():
    alarm_column = f"{sensor}_alarm"
    df[alarm_column] = ~df[sensor].between(low, high)
    alarm_columns.append(alarm_column)

# 3. 각 행의 전체 경보 개수를 계산한다.
df["alarm_count"] = df[alarm_columns].sum(axis=1)
df["process_alarm"] = df["alarm_count"] > 0

# 4. Lot별 상태 요약을 만든다.
summary = (
    df.groupby("lot_id")
    .agg(
        row_count=("timestamp", "size"),
        start_time=("timestamp", "min"),
        end_time=("timestamp", "max"),
        alarm_rows=("process_alarm", "sum"),
        max_simultaneous_alarms=("alarm_count", "max"),
        mean_temperature_c=("temperature_c", "mean"),
        mean_pressure_kpa=("pressure_kpa", "mean"),
        mean_vibration_rms=("vibration_rms", "mean"),
        mean_motor_current_a=("motor_current_a", "mean"),
    )
    .reset_index()
)

# 5. 경보 비율을 계산한다.
summary["alarm_rate_percent"] = (
    summary["alarm_rows"] / summary["row_count"] * 100.0
)

# 6. 교육용 상태 등급을 부여한다.
def classify_health(alarm_rate):
    if alarm_rate < 1.0:
        return "NORMAL"
    if alarm_rate < 5.0:
        return "WATCH"
    return "ALERT"

summary["health_status"] = summary[
    "alarm_rate_percent"
].apply(classify_health)

# 7. CSV와 JSON으로 저장한다.
summary.to_csv(CSV_OUTPUT, index=False, encoding="utf-8-sig")

records = summary.copy()
for column in ["start_time", "end_time"]:
    records[column] = records[column].astype(str)

JSON_OUTPUT.write_text(
    json.dumps(
        records.to_dict(orient="records"),
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)

print(summary.round(3))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] JSON: {JSON_OUTPUT}")
