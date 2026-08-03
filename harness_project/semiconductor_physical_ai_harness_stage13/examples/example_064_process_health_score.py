"""
반도체 Physical AI 하네스 엔지니어링 실습 061~065
Windows 10 / Anaconda / Pandas / NumPy / Matplotlib
다변량 공정 모니터링
"""

from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "outputs" / "combined_multisensor_alerts.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "process_health_score.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

zscore_columns = [
    "temperature_c_zscore",
    "pressure_kpa_zscore",
    "gas_flow_sccm_zscore",
    "vibration_rms_zscore",
    "motor_current_a_zscore",
]

# 1. 센서 Z-score 절댓값의 평균으로 전체 편차 수준을 계산한다.
df["mean_absolute_zscore"] = (
    df[zscore_columns]
    .abs()
    .mean(axis=1)
)

# 2. T²를 임계값으로 나눈 비율을 계산한다.
df["t2_ratio"] = (
    df["hotelling_t2"]
    / df["t2_threshold"]
)

# 3. 센서 편차와 T² 비율을 결합한 위험 점수를 만든다.
df["risk_score"] = (
    0.55 * df["mean_absolute_zscore"]
    + 0.45 * df["t2_ratio"]
)

# 4. 위험 점수를 0~100 상태 점수로 변환한다.
df["process_health_score"] = (
    100.0
    - 25.0 * df["risk_score"]
).clip(lower=0.0, upper=100.0)

def classify_health(score):
    if score >= 85.0:
        return "HEALTHY"
    if score >= 70.0:
        return "WATCH"
    if score >= 50.0:
        return "DEGRADED"
    return "CRITICAL"

df["process_health_status"] = (
    df["process_health_score"]
    .apply(classify_health)
)

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[공정 상태 등급별 건수]")
print(df["process_health_status"].value_counts())
print()
print(
    "주의: 상태 점수와 가중치는 교육용이며 "
    "실제 공정 승인 기준이 아닙니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
