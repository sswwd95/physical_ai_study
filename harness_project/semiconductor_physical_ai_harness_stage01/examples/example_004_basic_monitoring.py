"""
반도체 Physical AI 하네스 엔지니어링 실습
Windows 10 / Anaconda / PyMC
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
csv_path = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
output_path = PROJECT_ROOT / "outputs" / "basic_monitoring_result.csv"

# 1. 센서 데이터를 읽는다.
df = pd.read_csv(csv_path, parse_dates=["timestamp"])

# 2. 현장 엔지니어가 정한 초기 경보 기준을 정의한다.
LIMITS = {
    "temperature_c": (62.0, 69.0),
    "pressure_kpa": (99.5, 103.0),
    "gas_flow_sccm": (485.0, 515.0),
    "vibration_rms": (0.0, 2.5),
    "motor_current_a": (0.0, 9.0),
}

# 3. 각 센서가 정상 범위를 벗어났는지 True/False로 표시한다.
alarm_columns = []
for sensor, (low, high) in LIMITS.items():
    alarm_column = f"{sensor}_alarm"
    df[alarm_column] = ~df[sensor].between(low, high)
    alarm_columns.append(alarm_column)

# 4. 하나라도 경보가 발생하면 전체 공정 경보를 True로 만든다.
df["process_alarm"] = df[alarm_columns].any(axis=1)

# 5. 경보 원인을 사람이 읽기 쉬운 문자열로 만든다.
def collect_alarm_reasons(row):
    reasons = []
    for sensor in LIMITS:
        if row[f"{sensor}_alarm"]:
            reasons.append(sensor)
    return ",".join(reasons)

df["alarm_reason"] = df.apply(collect_alarm_reasons, axis=1)

# 6. 결과를 저장하고 핵심 요약을 출력한다.
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print("전체 행:", len(df))
print("경보 행:", int(df["process_alarm"].sum()))
print(df.loc[df["process_alarm"], [
    "timestamp", "process_alarm", "alarm_reason"
]].head(10))
print(f"[완료] 결과 저장: {output_path}")
