"""
반도체 Physical AI 하네스 엔지니어링 실습 031~035
Windows 10 / Anaconda / Pandas
단위, 시간축, 중복, 드리프트 데이터 품질
"""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import linregress

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_canonical.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "sensor_drift_summary.csv"
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

window_size = 120
rows = []

# 1. 최근 120초 구간의 선형 추세를 계산한다.
recent = df.tail(window_size).copy()
x = np.arange(len(recent), dtype=float)

for sensor in sensor_columns:
    regression = linregress(
        x,
        recent[sensor].to_numpy(),
    )

    slope_per_sample = float(regression.slope)
    slope_per_minute = (
        slope_per_sample * 60.0
    )

    # 2. 센서별 교육용 드리프트 임계값을 정의한다.
    thresholds_per_minute = {
        "temperature_c": 0.20,
        "pressure_kpa": 0.10,
        "gas_flow_sccm": 1.00,
        "vibration_rms": 0.05,
        "motor_current_a": 0.05,
    }

    threshold = thresholds_per_minute[sensor]
    drift_detected = (
        abs(slope_per_minute) >= threshold
        and regression.pvalue < 0.05
    )

    rows.append(
        {
            "sensor": sensor,
            "window_samples": window_size,
            "slope_per_sample": slope_per_sample,
            "slope_per_minute": slope_per_minute,
            "r_value": float(regression.rvalue),
            "p_value": float(regression.pvalue),
            "threshold_per_minute": threshold,
            "drift_detected": drift_detected,
        }
    )

# 3. 결과를 저장한다.
result = pd.DataFrame(rows)
result = result.sort_values(
    "slope_per_minute",
    key=lambda series: series.abs(),
    ascending=False,
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[최근 구간 센서 드리프트 요약]")
print(result.round(6))
print()
print(
    "주의: 선형 기울기는 기초 탐지 방법이며 "
    "공정 전환과 실제 센서 드리프트를 구분해야 합니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
