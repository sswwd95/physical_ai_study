"""
반도체 Physical AI 하네스 엔지니어링 실습 061~065
Windows 10 / Anaconda / Pandas / NumPy / Matplotlib
다변량 공정 모니터링
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "multisensor_process_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "multisensor_zscore_monitoring.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 초기 300개 샘플을 다중 센서 기준 구간으로 사용한다.
baseline = df[sensor_columns].iloc[:300]

means = baseline.mean()
stds = baseline.std(ddof=1)

result = df.copy()

# 2. 센서별 기준 평균과 표준편차로 Z-score를 계산한다.
for sensor in sensor_columns:
    result[f"{sensor}_zscore"] = (
        result[sensor] - means[sensor]
    ) / stds[sensor]

# 3. |Z|>=3을 센서별 경보로 표시한다.
alarm_columns = []

for sensor in sensor_columns:
    alarm_column = f"{sensor}_alarm"
    result[alarm_column] = (
        result[f"{sensor}_zscore"].abs() >= 3.0
    )
    alarm_columns.append(alarm_column)

# 4. 한 시각의 경보 센서 개수를 계산한다.
result["sensor_alarm_count"] = (
    result[alarm_columns].sum(axis=1)
)

result["any_sensor_alarm"] = (
    result["sensor_alarm_count"] > 0
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[센서별 경보 개수]")
print(result[alarm_columns].sum())
print()
print("전체 경보 행 수:", int(result["any_sensor_alarm"].sum()))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
