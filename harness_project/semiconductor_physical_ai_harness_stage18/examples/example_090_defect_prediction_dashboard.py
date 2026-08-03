"""
반도체 Physical AI 하네스 엔지니어링 실습 086~090
Windows 10 / Anaconda / Pandas / scikit-learn
로지스틱 회귀 기반 불량 예측
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PREDICTION_PATH = PROJECT_ROOT / "outputs" / "logistic_test_predictions.csv"
METRICS_PATH = PROJECT_ROOT / "outputs" / "logistic_evaluation_metrics.json"
BEST_PATH = PROJECT_ROOT / "outputs" / "best_threshold.json"
EFFECT_PATH = PROJECT_ROOT / "outputs" / "logistic_feature_effects.csv"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "defect_prediction_dashboard.html"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "defect_prediction_dashboard_summary.json"

pred = pd.read_csv(
    PREDICTION_PATH,
    parse_dates=["timestamp"],
)
metrics = json.loads(
    METRICS_PATH.read_text(encoding="utf-8")
)
best = json.loads(
    BEST_PATH.read_text(encoding="utf-8")
)
effects = pd.read_csv(EFFECT_PATH)

selected_threshold = float(
    best["selected_threshold"]
)

pred["selected_threshold_prediction"] = (
    pred["defect_probability"]
    >= selected_threshold
).astype(int)

# 1. Lot별 평균 위험과 예측 불량률을 집계한다.
lot_summary = (
    pred.groupby("lot_id")
    .agg(
        wafer_count=("wafer_id", "size"),
        actual_defect_rate_percent=(
            "defect_flag",
            lambda series: series.mean() * 100.0,
        ),
        predicted_defect_rate_percent=(
            "selected_threshold_prediction",
            lambda series: series.mean() * 100.0,
        ),
        mean_defect_probability=(
            "defect_probability",
            "mean",
        ),
        maximum_defect_probability=(
            "defect_probability",
            "max",
        ),
    )
    .reset_index()
)

high_risk_wafers = (
    pred.sort_values(
        "defect_probability",
        ascending=False,
    )
    .head(15)
    [
        [
            "wafer_id",
            "lot_id",
            "recipe_id",
            "tool_id",
            "defect_flag",
            "defect_probability",
        ]
    ]
)

top_effects = effects.head(12)

summary = {
    "test_rows": len(pred),
    "actual_defect_count": int(pred["defect_flag"].sum()),
    "selected_threshold": selected_threshold,
    "roc_auc": float(metrics["roc_auc"]),
    "average_precision": float(metrics["average_precision"]),
    "selected_threshold_recall": float(best["recall"]),
    "selected_threshold_precision": float(best["precision"]),
    "selected_threshold_f1": float(best["f1"]),
}

JSON_OUTPUT.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

lot_table = lot_summary.round(4).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
risk_table = high_risk_wafers.round(4).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
effect_table = top_effects[
    [
        "feature",
        "coefficient",
        "odds_ratio",
        "effect_direction",
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
<title>불량 예측 대시보드</title>
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
<h1>반도체 Physical AI 불량 예측 대시보드</h1>

<div class="kpi-grid">
  <div class="card">
    <div class="label">ROC-AUC</div>
    <div class="value">{metrics["roc_auc"]:.3f}</div>
  </div>
  <div class="card">
    <div class="label">Average Precision</div>
    <div class="value">{metrics["average_precision"]:.3f}</div>
  </div>
  <div class="card">
    <div class="label">선택 임계값</div>
    <div class="value">{selected_threshold:.2f}</div>
  </div>
  <div class="card">
    <div class="label">선택 Recall</div>
    <div class="value">{best["recall"]:.3f}</div>
  </div>
</div>

<div class="card">
  <h2>Lot별 실제·예측 불량 위험</h2>
  {lot_table}
</div>

<div class="card">
  <h2>예측 위험 상위 Wafer</h2>
  {risk_table}
</div>

<div class="card">
  <h2>로지스틱 회귀 특징 영향도</h2>
  {effect_table}
</div>

<div class="card note">
예측 확률과 계수는 공정 조사 우선순위를 위한 교육용 결과입니다.
실제 Wafer 폐기, 장비 정지, Recipe 변경에는 독립적인 품질 검증과 승인 절차가 필요합니다.
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
