"""
반도체 Physical AI 하네스 엔지니어링 실습 056~060
Windows 10 / Anaconda / Pandas / Matplotlib
EWMA, CUSUM, 작은 평균 이동, 통합 공정 경보
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "temperature_shift_log.csv"
EWMA_PATH = PROJECT_ROOT / "outputs" / "ewma_control_chart.csv"
CUSUM_PATH = PROJECT_ROOT / "outputs" / "cusum_control_chart.csv"
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "integrated_process_alerts.csv"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "integrated_process_alert_summary.json"

raw = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
ewma = pd.read_csv(EWMA_PATH, parse_dates=["timestamp"])
cusum = pd.read_csv(CUSUM_PATH, parse_dates=["timestamp"])

# 1. 개별값 3σ 경보를 계산한다.
baseline = raw["temperature_c"].iloc[:200]
mean_value = float(baseline.mean())
std_value = float(baseline.std(ddof=1))

individual_alert = (
    (raw["temperature_c"] > mean_value + 3.0 * std_value)
    | (raw["temperature_c"] < mean_value - 3.0 * std_value)
)

# 2. 세 가지 경보를 한 표에 결합한다.
result = raw.copy()
result["individual_alert"] = individual_alert
result["ewma_alert"] = ewma["ewma_alert"]
result["cusum_alert"] = cusum["cusum_alert"]

alert_columns = [
    "individual_alert",
    "ewma_alert",
    "cusum_alert",
]

# 3. 동시에 경보한 방법 수를 계산한다.
result["alert_vote_count"] = (
    result[alert_columns]
    .sum(axis=1)
)

# 4. 투표 수에 따라 교육용 경보 등급을 부여한다.
def classify_alert(vote_count):
    if vote_count == 0:
        return "NORMAL"
    if vote_count == 1:
        return "WATCH"
    if vote_count == 2:
        return "WARNING"
    return "CRITICAL"

result["integrated_alert_level"] = (
    result["alert_vote_count"]
    .apply(classify_alert)
)

result.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

# 5. 등급별 건수와 첫 발생 시각을 요약한다.
summary = {
    "total_rows": len(result),
    "level_counts": {
        level: int(
            (
                result["integrated_alert_level"]
                == level
            ).sum()
        )
        for level in [
            "NORMAL",
            "WATCH",
            "WARNING",
            "CRITICAL",
        ]
    },
    "first_non_normal_time": None,
}

non_normal = (
    result["integrated_alert_level"]
    != "NORMAL"
)

if non_normal.any():
    summary["first_non_normal_time"] = str(
        result.loc[
            non_normal,
            "timestamp",
        ].iloc[0]
    )

JSON_OUTPUT.write_text(
    json.dumps(
        summary,
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] JSON: {JSON_OUTPUT}")
