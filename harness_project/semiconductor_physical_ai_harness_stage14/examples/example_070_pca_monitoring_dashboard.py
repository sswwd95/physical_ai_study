"""
반도체 Physical AI 하네스 엔지니어링 실습 066~070
Windows 10 / Anaconda / Pandas / scikit-learn
PCA 기반 다변량 공정 모니터링
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCORE_PATH = PROJECT_ROOT / "outputs" / "pca_score_monitoring.csv"
SPE_PATH = PROJECT_ROOT / "outputs" / "spe_q_monitoring.csv"
CONTRIB_PATH = PROJECT_ROOT / "outputs" / "pca_sensor_contributions.csv"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "pca_monitoring_dashboard.html"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "pca_monitoring_summary.json"

score_df = pd.read_csv(
    SCORE_PATH,
    parse_dates=["timestamp"],
)

spe_df = pd.read_csv(
    SPE_PATH,
    parse_dates=["timestamp"],
)

contrib_df = pd.read_csv(
    CONTRIB_PATH,
    parse_dates=["timestamp"],
)

# 1. 핵심 KPI를 계산한다.
pc_alert_rows = int(
    score_df["any_pc_score_alert"].sum()
)

spe_alert_rows = int(
    spe_df["spe_q_alert"].sum()
)

both_alert_rows = int(
    (
        score_df["any_pc_score_alert"]
        & spe_df["spe_q_alert"]
    ).sum()
)

latest_spe = float(
    spe_df["spe_q"].iloc[-1]
)

# 2. Lot별 경보를 요약한다.
combined = score_df[
    ["timestamp", "lot_id", "recipe_id", "any_pc_score_alert"]
].copy()

combined["spe_q_alert"] = spe_df["spe_q_alert"]
combined["spe_q"] = spe_df["spe_q"]

lot_summary = (
    combined.groupby("lot_id")
    .agg(
        row_count=("timestamp", "size"),
        pc_score_alert_rows=("any_pc_score_alert", "sum"),
        spe_alert_rows=("spe_q_alert", "sum"),
        maximum_spe_q=("spe_q", "max"),
    )
    .reset_index()
)

top_contributions = (
    contrib_df["top_contribution_sensor"]
    .value_counts()
    .rename_axis("sensor")
    .reset_index(name="alert_contribution_count")
)

lot_table_html = lot_summary.round(4).to_html(
    index=False,
    border=0,
    classes="summary-table",
)

contribution_table_html = (
    top_contributions.to_html(
        index=False,
        border=0,
        classes="summary-table",
    )
)

summary = {
    "total_rows": len(score_df),
    "pc_score_alert_rows": pc_alert_rows,
    "spe_alert_rows": spe_alert_rows,
    "both_alert_rows": both_alert_rows,
    "latest_spe_q": latest_spe,
    "top_contribution_sensor": (
        None
        if top_contributions.empty
        else str(top_contributions.iloc[0]["sensor"])
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
<title>PCA 다변량 공정 모니터링</title>
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
    margin-top: 16px;
    color: #666;
    font-size: 13px;
}}
</style>
</head>
<body>
<h1>반도체 Physical AI PCA 모니터링</h1>

<div class="kpi-grid">
  <div class="card">
    <div class="label">PC 점수 경보</div>
    <div class="value">{pc_alert_rows}</div>
  </div>
  <div class="card">
    <div class="label">SPE/Q 경보</div>
    <div class="value">{spe_alert_rows}</div>
  </div>
  <div class="card">
    <div class="label">동시 경보</div>
    <div class="value">{both_alert_rows}</div>
  </div>
  <div class="card">
    <div class="label">최신 SPE/Q</div>
    <div class="value">{latest_spe:.3f}</div>
  </div>
</div>

<div class="card">
  <h2>Lot별 PCA 경보 요약</h2>
  {lot_table_html}
</div>

<div class="card">
  <h2>SPE 경보 센서 기여도</h2>
  {contribution_table_html}
</div>

<div class="note">
PCA 기준 구간, 설명분산, SPE/Q 임계값은 교육용입니다.
실제 Fab에서는 제품·Recipe·장비별 모델 검증이 필요합니다.
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
