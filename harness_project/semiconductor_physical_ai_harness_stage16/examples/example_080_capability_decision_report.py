"""
반도체 Physical AI 하네스 엔지니어링 실습 076~080
Windows 10 / Anaconda / Pandas / SciPy
공정 능력 불확실성과 비정규 분포
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "outputs" / "capability_uncertainty_comparison.csv"
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "capability_decision_report.csv"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "capability_decision_report.html"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "capability_decision_summary.json"

df = pd.read_csv(INPUT_PATH)

def classify(row):
    index_value = row["recommended_capability_index"]
    lower_bound = row["cpk_ci_2_5_percent"]

    if index_value >= 1.33 and lower_bound >= 1.0:
        return "CAPABLE"
    if index_value >= 1.0:
        return "MARGINAL"
    return "NOT_CAPABLE"

df["capability_decision"] = df.apply(
    classify,
    axis=1,
)

df["review_required"] = (
    df["normality_rejected_at_0_05"]
    | (df["cpk_ci_2_5_percent"] < 1.0)
)

df.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

summary = {
    "metric_count": len(df),
    "decision_counts": {
        key: int(value)
        for key, value in
        df["capability_decision"]
        .value_counts()
        .to_dict()
        .items()
    },
    "review_required_count": int(
        df["review_required"].sum()
    ),
}

JSON_OUTPUT.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

table_html = df[
    [
        "metric",
        "recommended_method",
        "recommended_capability_index",
        "cpk_ci_2_5_percent",
        "cpk_ci_97_5_percent",
        "capability_decision",
        "review_required",
    ]
].round(4).to_html(
    index=False,
    border=0,
    classes="summary-table",
)

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>공정 능력 불확실성 종합 판정</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 30px;
    background: #f4f6f8;
}}
.card {{
    background: white;
    padding: 18px;
    border-radius: 10px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
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
<h1>반도체 Physical AI 공정 능력 종합 판정</h1>

<div class="card">
  <p>분석 지표 수: {len(df)}</p>
  <p>추가 검토 필요: {summary["review_required_count"]}</p>
</div>

<div class="card">
  <h2>지표별 판정</h2>
  {table_html}
</div>

<div class="card note">
정규성 검정, 분위수 기반 지수, Bootstrap 신뢰구간은 교육용 판정 보조 수단입니다.
실제 Fab 승인에는 측정시스템 분석, 공정 안정성, 고객 규격과 표본 설계를 함께 검토해야 합니다.
</div>
</body>
</html>
"""

HTML_OUTPUT.write_text(
    html,
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] HTML: {HTML_OUTPUT}")
print(f"[완료] JSON: {JSON_OUTPUT}")
