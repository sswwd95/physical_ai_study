"""
반도체 Physical AI 하네스 엔지니어링 실습 056~060
Windows 10 / Anaconda / Pandas / Matplotlib
EWMA, CUSUM, 작은 평균 이동, 통합 공정 경보
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "temperature_shift_log.csv"
EWMA_PATH = PROJECT_ROOT / "outputs" / "ewma_control_chart.csv"
CUSUM_PATH = PROJECT_ROOT / "outputs" / "cusum_control_chart.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "small_shift_detection_summary.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
ewma = pd.read_csv(EWMA_PATH, parse_dates=["timestamp"])
cusum = pd.read_csv(CUSUM_PATH, parse_dates=["timestamp"])

# 1. 합성 데이터에 주입된 작은 평균 이동 구간을 정의한다.
small_shift_start = df.loc[250, "timestamp"]
small_shift_end = df.loc[429, "timestamp"]

# 2. 이동 구간 이후 첫 경보 시각을 찾는다.
def first_alert_time(
    frame,
    alert_column,
):
    mask = (
        (frame["timestamp"] >= small_shift_start)
        & (frame["timestamp"] <= small_shift_end)
        & frame[alert_column]
    )

    if not mask.any():
        return None

    return frame.loc[
        mask,
        "timestamp",
    ].iloc[0]

ewma_first = first_alert_time(
    ewma,
    "ewma_alert",
)

cusum_first = first_alert_time(
    cusum,
    "cusum_alert",
)

# 3. 이동 시작부터 경보까지 지연 시간을 계산한다.
rows = []

for method, alert_time in [
    ("EWMA", ewma_first),
    ("CUSUM", cusum_first),
]:
    if alert_time is None:
        delay_sec = None
        detected = False
    else:
        delay_sec = float(
            (
                alert_time - small_shift_start
            ).total_seconds()
        )
        detected = True

    rows.append(
        {
            "method": method,
            "shift_start": small_shift_start,
            "shift_end": small_shift_end,
            "detected": detected,
            "first_alert_time": alert_time,
            "detection_delay_sec": delay_sec,
        }
    )

result = pd.DataFrame(rows)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[작은 평균 이동 탐지 요약]")
print(result)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
