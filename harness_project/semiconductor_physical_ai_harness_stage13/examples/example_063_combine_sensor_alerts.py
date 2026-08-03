"""
반도체 Physical AI 하네스 엔지니어링 실습 061~065
Windows 10 / Anaconda / Pandas / NumPy / Matplotlib
다변량 공정 모니터링
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ZSCORE_PATH = PROJECT_ROOT / "outputs" / "multisensor_zscore_monitoring.csv"
T2_PATH = PROJECT_ROOT / "outputs" / "hotelling_t2_monitoring.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "combined_multisensor_alerts.csv"

zscore_df = pd.read_csv(
    ZSCORE_PATH,
    parse_dates=["timestamp"],
)

t2_df = pd.read_csv(
    T2_PATH,
    parse_dates=["timestamp"],
)

# 1. 두 결과의 timestamp가 같은 순서인지 검사한다.
if not zscore_df["timestamp"].equals(
    t2_df["timestamp"]
):
    raise ValueError(
        "Z-score와 T² 결과의 timestamp가 일치하지 않습니다."
    )

result = zscore_df.copy()

# 2. Hotelling T² 결과를 결합한다.
result["hotelling_t2"] = t2_df["hotelling_t2"]
result["t2_threshold"] = t2_df["t2_threshold"]
result["t2_alert"] = t2_df["t2_alert"]

# 3. 단변량 센서 경보와 다변량 경보를 결합한다.
result["combined_vote_count"] = (
    result["sensor_alarm_count"]
    + result["t2_alert"].astype(int)
)

def classify_level(row):
    if row["combined_vote_count"] == 0:
        return "NORMAL"
    if row["combined_vote_count"] == 1:
        return "WATCH"
    if row["combined_vote_count"] <= 3:
        return "WARNING"
    return "CRITICAL"

result["combined_alert_level"] = result.apply(
    classify_level,
    axis=1,
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[통합 경보 등급별 건수]")
print(result["combined_alert_level"].value_counts())
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
