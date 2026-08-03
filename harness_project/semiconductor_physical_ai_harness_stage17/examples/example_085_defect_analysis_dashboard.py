"""
반도체 Physical AI 하네스 엔지니어링 실습 081~085
Windows 10 / Anaconda / Pandas / SciPy
불량 라벨, 불량률, 교차표, 위험비 분석
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "wafer_process_quality.csv"
BIN_PATH = PROJECT_ROOT / "outputs" / "feature_bin_defect_rates.csv"
CHI_PATH = PROJECT_ROOT / "outputs" / "chi_square_crosstab_summary.csv"
RR_PATH = PROJECT_ROOT / "outputs" / "condition_risk_ratios.csv"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "defect_analysis_dashboard.html"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "defect_analysis_summary.json"

df = pd.read_csv(DATA_PATH)
bin_df = pd.read_csv(BIN_PATH)
chi_df = pd.read_csv(CHI_PATH)
rr_df = pd.read_csv(RR_PATH)

overall_defect_rate = float(
    df["defect_flag"].mean() * 100.0
)

highest_risk = rr_df.iloc[0]

recipe_summary = (
    df.groupby("recipe_id")
    .agg(
        sample_count=("defect_flag", "size"),
        defect_count=("defect_flag", "sum"),
        defect_rate_percent=("defect_flag", lambda s: s.mean() * 100.0),
    )
    .reset_index()
)

tool_summary = (
    df.groupby("tool_id")
    .agg(
        sample_count=("defect_flag", "size"),
        defect_count=("defect_flag", "sum"),
        defect_rate_percent=("defect_flag", lambda s: s.mean() * 100.0),
    )
    .reset_index()
)

summary = {
    "total_wafers": len(df),
    "defect_count": int(df["defect_flag"].sum()),
    "overall_defect_rate_percent": overall_defect_rate,
    "highest_risk_condition": str(highest_risk["condition"]),
    "highest_risk_ratio": float(highest_risk["risk_ratio"]),
    "significant_categorical_conditions": chi_df.loc[
        chi_df["association_detected_at_0_05"],
        "condition",
    ].tolist(),
}

JSON_OUTPUT.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

recipe_table = recipe_summary.round(4).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
tool_table = tool_summary.round(4).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
risk_table = rr_df.round(4).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
bin_table = (
    bin_df.sort_values(
        "defect_rate_percent",
        ascending=False,
    )
    .head(12)
    .round(4)
    .to_html(
        index=False,
        border=0,
        classes="summary-table",
    )
)

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>반도체 불량 분석 대시보드</title>
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
    margin-bottom: 16px;
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
    width: 100%;
    border-collapse: collapse;
}}
.summary-table th,
.summary-table td {{
    padding: 9px;
    border-bottom: 1px solid #ddd;
    text-align: right;
}}
.summary-table th:first-child,
.summary-table td:first-child {{
    text-align: left;
}}
.note {{
    color: #666;
    font-size: 13px;
}}
</style>
</head>
<body>
<h1>반도체 Physical AI 불량 분석 대시보드</h1>

<div class="kpi-grid">
  <div class="card">
    <div class="label">전체 Wafer</div>
    <div class="value">{len(df)}</div>
  </div>
  <div class="card">
    <div class="label">불량 수</div>
    <div class="value">{int(df["defect_flag"].sum())}</div>
  </div>
  <div class="card">
    <div class="label">불량률</div>
    <div class="value">{overall_defect_rate:.2f}%</div>
  </div>
  <div class="card">
    <div class="label">최고 위험 조건</div>
    <div class="value">{highest_risk["condition"]}</div>
  </div>
</div>

<div class="card">
  <h2>Recipe별 불량률</h2>
  {recipe_table}
</div>

<div class="card">
  <h2>Tool별 불량률</h2>
  {tool_table}
</div>

<div class="card">
  <h2>조건별 위험비</h2>
  {risk_table}
</div>

<div class="card">
  <h2>센서 구간별 높은 불량률</h2>
  {bin_table}
</div>

<div class="card note">
카이제곱 검정과 위험비는 연관성 탐색 도구입니다.
공정 원인과 인과관계는 DOE, 장비 이력, 공정 전문가 검토로 확인해야 합니다.
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
