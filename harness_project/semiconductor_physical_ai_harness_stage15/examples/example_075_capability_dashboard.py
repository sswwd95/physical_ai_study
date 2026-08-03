"""
반도체 Physical AI 하네스 엔지니어링 실습 071~075
Windows 10 / Anaconda / Pandas / Matplotlib
공정 능력지수와 규격 이탈 분석
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOT_PATH = PROJECT_ROOT / "outputs" / "lot_capability_comparison.csv"
CP_PATH = PROJECT_ROOT / "outputs" / "cp_cpk_summary.json"
PP_PATH = PROJECT_ROOT / "outputs" / "pp_ppk_summary.json"
OOS_PATH = PROJECT_ROOT / "outputs" / "spec_violation_summary.json"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "process_capability_dashboard.html"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "process_capability_dashboard_summary.json"

lot_df = pd.read_csv(LOT_PATH)
cp = json.loads(CP_PATH.read_text(encoding="utf-8"))
pp = json.loads(PP_PATH.read_text(encoding="utf-8"))
oos = json.loads(OOS_PATH.read_text(encoding="utf-8"))

# 1. 핵심 KPI와 최저 Lot을 계산한다.
worst_lot_row = lot_df.sort_values("cpk").iloc[0]

summary = {
    "cp": float(cp["cp"]),
    "cpk": float(cp["cpk"]),
    "pp": float(pp["pp"]),
    "ppk": float(pp["ppk"]),
    "out_of_spec_rate_percent": float(
        oos["out_of_spec_rate_percent"]
    ),
    "ppm_observed": float(oos["ppm_observed"]),
    "worst_lot_id": str(worst_lot_row["lot_id"]),
    "worst_lot_cpk": float(worst_lot_row["cpk"]),
}

JSON_OUTPUT.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

lot_table = lot_df.round(4).to_html(
    index=False,
    border=0,
    classes="summary-table",
)

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>공정 능력 대시보드</title>
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
<h1>반도체 Physical AI 공정 능력 대시보드</h1>

<div class="kpi-grid">
  <div class="card">
    <div class="label">Cp / Cpk</div>
    <div class="value">{cp["cp"]:.3f} / {cp["cpk"]:.3f}</div>
  </div>
  <div class="card">
    <div class="label">Pp / Ppk</div>
    <div class="value">{pp["pp"]:.3f} / {pp["ppk"]:.3f}</div>
  </div>
  <div class="card">
    <div class="label">규격 이탈률</div>
    <div class="value">{oos["out_of_spec_rate_percent"]:.3f}%</div>
  </div>
  <div class="card">
    <div class="label">관측 PPM</div>
    <div class="value">{oos["ppm_observed"]:.1f}</div>
  </div>
</div>

<div class="card">
  <h2>Lot별 공정 능력 비교</h2>
  {lot_table}
</div>

<div class="card">
  <h2>우선 개선 대상</h2>
  <p>최저 Cpk Lot: {worst_lot_row["lot_id"]}</p>
  <p>Cpk: {worst_lot_row["cpk"]:.4f}</p>
</div>

<div class="note">
공정 능력지수는 공정이 통계적으로 안정적이고 측정시스템이 신뢰할 수 있을 때 해석해야 합니다.
본 기준은 교육용이며 실제 고객·Fab 승인 기준이 아닙니다.
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
