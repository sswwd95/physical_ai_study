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
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "control_chart_performance.csv"

raw = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
ewma = pd.read_csv(EWMA_PATH, parse_dates=["timestamp"])
cusum = pd.read_csv(CUSUM_PATH, parse_dates=["timestamp"])

# 1. 기준 구간과 이동 구간을 정의한다.
baseline_end = raw.loc[199, "timestamp"]

shift_ranges = [
    (
        "small_shift",
        raw.loc[250, "timestamp"],
        raw.loc[429, "timestamp"],
    ),
    (
        "large_shift",
        raw.loc[520, "timestamp"],
        raw.loc[619, "timestamp"],
    ),
]

rows = []

# 2. 각 방법의 기준 구간 오경보율을 계산한다.
for method, frame, alert_column in [
    ("EWMA", ewma, "ewma_alert"),
    ("CUSUM", cusum, "cusum_alert"),
]:
    baseline_mask = (
        frame["timestamp"] <= baseline_end
    )

    false_alarm_count = int(
        frame.loc[
            baseline_mask,
            alert_column,
        ].sum()
    )

    false_alarm_rate = float(
        frame.loc[
            baseline_mask,
            alert_column,
        ].mean()
        * 100.0
    )

    for shift_name, start_time, end_time in shift_ranges:
        shift_mask = (
            (frame["timestamp"] >= start_time)
            & (frame["timestamp"] <= end_time)
        )

        alert_mask = (
            shift_mask
            & frame[alert_column]
        )

        if alert_mask.any():
            first_alert = frame.loc[
                alert_mask,
                "timestamp",
            ].iloc[0]

            delay_sec = float(
                (
                    first_alert - start_time
                ).total_seconds()
            )

            detected = True
        else:
            first_alert = None
            delay_sec = None
            detected = False

        rows.append(
            {
                "method": method,
                "shift_name": shift_name,
                "detected": detected,
                "detection_delay_sec": delay_sec,
                "false_alarm_count_baseline": false_alarm_count,
                "false_alarm_rate_baseline_percent": false_alarm_rate,
            }
        )

result = pd.DataFrame(rows)
result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[관리도 성능 비교]")
print(result)
print()
print(
    "탐지 지연이 짧을수록 빠르지만, "
    "기준 구간 오경보율도 함께 확인해야 합니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
