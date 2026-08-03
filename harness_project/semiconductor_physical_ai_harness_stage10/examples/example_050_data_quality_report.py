"""
반도체 Physical AI 하네스 엔지니어링 실습 046~050
Windows 10 / Anaconda / Pandas / scikit-learn
시계열 분할, 누출 방지, 전처리 재사용, 품질 리포트
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "data_quality_metrics.csv"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "data_quality_report.html"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

physical_ranges = {
    "temperature_c": (0.0, 150.0),
    "pressure_kpa": (80.0, 130.0),
    "gas_flow_sccm": (0.0, 1000.0),
    "vibration_rms": (0.0, 20.0),
    "motor_current_a": (0.0, 50.0),
}

rows = []

# 1. 센서별 결측·범위 위반·중복 영향 지표를 만든다.
for sensor in sensor_columns:
    low, high = physical_ranges[sensor]

    rows.append({
        "sensor": sensor,
        "missing_count": int(df[sensor].isna().sum()),
        "missing_rate_percent": float(
            df[sensor].isna().mean() * 100.0
        ),
        "range_violation_count": int(
            (~df[sensor].between(low, high)).sum()
        ),
        "mean": float(df[sensor].mean()),
        "std": float(df[sensor].std()),
    })

metrics = pd.DataFrame(rows)
metrics.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

# 2. 전체 데이터 품질 KPI를 계산한다.
duplicate_timestamp_count = int(
    df["timestamp"].duplicated().sum()
)

timestamp_sorted = df.sort_values("timestamp")
interval_sec = (
    timestamp_sorted["timestamp"]
    .diff()
    .dt.total_seconds()
)

gap_count = int((interval_sec > 1.01).sum())

total_missing = int(
    df[sensor_columns].isna().sum().sum()
)

total_range_violations = int(
    sum(
        (~df[sensor].between(*physical_ranges[sensor])).sum()
        for sensor in sensor_columns
    )
)

quality_score = 100.0
quality_score -= min(total_missing * 0.5, 20.0)
quality_score -= min(total_range_violations * 2.0, 30.0)
quality_score -= min(duplicate_timestamp_count * 2.0, 20.0)
quality_score -= min(gap_count * 1.0, 20.0)
quality_score = max(0.0, quality_score)

table_html = metrics.round(4).to_html(
    index=False,
    border=0,
    classes="quality-table",
)

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>반도체 센서 데이터 품질 리포트</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 30px;
    background: #f5f6f8;
}}
.card {{
    background: white;
    padding: 18px;
    border-radius: 10px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}}
.score {{
    font-size: 36px;
    font-weight: bold;
}}
.quality-table {{
    width: 100%;
    border-collapse: collapse;
}}
.quality-table th,
.quality-table td {{
    border-bottom: 1px solid #ddd;
    padding: 9px;
    text-align: right;
}}
.quality-table th:first-child,
.quality-table td:first-child {{
    text-align: left;
}}
</style>
</head>
<body>
<h1>반도체 Physical AI 데이터 품질 종합 리포트</h1>

<div class="card">
  <div>교육용 데이터 품질 점수</div>
  <div class="score">{quality_score:.1f} / 100</div>
</div>

<div class="card">
  <p>전체 행: {len(df)}</p>
  <p>전체 결측값: {total_missing}</p>
  <p>물리 범위 위반: {total_range_violations}</p>
  <p>중복 timestamp: {duplicate_timestamp_count}</p>
  <p>시간 간격 누락 후보: {gap_count}</p>
</div>

<div class="card">
  <h2>센서별 품질 지표</h2>
  {table_html}
</div>

<div class="card">
  본 점수와 기준은 교육용이며 실제 Fab 승인 기준이 아닙니다.
</div>
</body>
</html>
"""

HTML_OUTPUT.write_text(html, encoding="utf-8")

print("[데이터 품질 KPI]")
print("품질 점수:", round(quality_score, 2))
print("전체 결측:", total_missing)
print("범위 위반:", total_range_violations)
print("중복 timestamp:", duplicate_timestamp_count)
print("시간 간격 누락 후보:", gap_count)
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] HTML: {HTML_OUTPUT}")
