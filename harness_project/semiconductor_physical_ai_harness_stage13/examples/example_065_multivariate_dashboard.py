"""
반도체 Physical AI 하네스 엔지니어링 실습 061~065
Windows 10 / Anaconda / Pandas / NumPy / Matplotlib
다변량 공정 모니터링
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "outputs" / "process_health_score.csv"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "multivariate_monitoring_dashboard.html"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "multivariate_monitoring_summary.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 전체 KPI를 계산한다.
mean_health_score = float(
    df["process_health_score"].mean()
)

critical_rows = int(
    (
        df["process_health_status"]
        == "CRITICAL"
    ).sum()
)

warning_or_higher = int(
    df["combined_alert_level"]
    .isin(["WARNING", "CRITICAL"])
    .sum()
)

t2_alert_rows = int(
    df["t2_alert"].sum()
)

latest = df.iloc[-1]

# 2. Lot별 공정 상태를 집계한다.
lot_summary = (
    df.groupby("lot_id")
    .agg(
        row_count=("timestamp", "size"),
        mean_health_score=("process_health_score", "mean"),
        minimum_health_score=("process_health_score", "min"),
        t2_alert_rows=("t2_alert", "sum"),
        max_sensor_alarm_count=("sensor_alarm_count", "max"),
    )
    .reset_index()
)

table_html = lot_summary.round(3).to_html(
    index=False,
    border=0,
    classes="summary-table",
)

summary = {
    "total_rows": len(df),
    "mean_health_score": mean_health_score,
    "critical_rows": critical_rows,
    "warning_or_higher_rows": warning_or_higher,
    "t2_alert_rows": t2_alert_rows,
    "latest_timestamp": str(latest["timestamp"]),
    "latest_health_score": float(
        latest["process_health_score"]
    ),
    "latest_health_status": str(
        latest["process_health_status"]
    ),
}

JSON_OUTPUT.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>다변량 공정 모니터링 대시보드</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 30px;
    background: #f4f6f8;
}}
.kpi-grid {{
    display: grid;
    grid-template-columns: repeat(4, minmax(150px, 1fr));
    gap: 14px;
    margin-bottom: 24px;
}}
.card {{
    background: white;
    border-radius: 10px;
    padding: 18px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}}
.label {{
    color: #666;
    font-size: 14px;
}}
.value {{
    font-size: 26px;
    font-weight: bold;
    margin-top: 8px;
}}
.summary-table {{
    border-collapse: collapse;
    width: 100%;
}}
.summary-table th,
.summary-table td {{
    border-bottom: 1px solid #ddd;
    padding: 9px;
    text-align: right;
}}
.summary-table th:first-child,
.summary-table td:first-child {{
    text-align: left;
}}
.note {{
    color: #666;
    font-size: 13px;
    margin-top: 16px;
}}
</style>
</head>
<body>
<h1>반도체 Physical AI 다변량 모니터링</h1>

<div class="kpi-grid">
  <div class="card">
    <div class="label">평균 상태 점수</div>
    <div class="value">{mean_health_score:.2f}</div>
  </div>
  <div class="card">
    <div class="label">T² 경보 행</div>
    <div class="value">{t2_alert_rows}</div>
  </div>
  <div class="card">
    <div class="label">WARNING 이상</div>
    <div class="value">{warning_or_higher}</div>
  </div>
  <div class="card">
    <div class="label">CRITICAL 행</div>
    <div class="value">{critical_rows}</div>
  </div>
</div>

<div class="card">
  <h2>최신 공정 상태</h2>
  <p>시각: {latest["timestamp"]}</p>
  <p>상태 점수: {latest["process_health_score"]:.2f}</p>
  <p>상태 등급: {latest["process_health_status"]}</p>
</div>

<div class="card">
  <h2>Lot별 다변량 상태 요약</h2>
  {table_html}
</div>

<div class="note">
Hotelling T² 임계값과 상태 점수는 교육용입니다.
실제 Fab 적용 전 공정·설비·품질 담당자의 검증이 필요합니다.
</div>
</body>
</html>
"""

HTML_OUTPUT.write_text(
    html,
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] HTML: {HTML_OUTPUT}")
print(f"[완료] JSON: {JSON_OUTPUT}")
