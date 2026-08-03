"""
반도체 Physical AI 하네스 엔지니어링 실습 091~095
Windows 10 / Anaconda / Pandas / scikit-learn
Decision Tree, Random Forest, 확률 보정, 특징 중요도
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
COMPARISON_PATH = PROJECT_ROOT / "outputs" / "model_comparison.csv"
CALIBRATION_PATH = PROJECT_ROOT / "outputs" / "probability_calibration_comparison.csv"
PREDICTION_PATH = PROJECT_ROOT / "outputs" / "calibrated_rf_predictions.csv"
IMPORTANCE_PATH = PROJECT_ROOT / "outputs" / "random_forest_permutation_importance.csv"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "ensemble_model_dashboard.html"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "ensemble_model_dashboard_summary.json"

comparison = pd.read_csv(COMPARISON_PATH)
calibration = pd.read_csv(CALIBRATION_PATH)
pred = pd.read_csv(PREDICTION_PATH, parse_dates=["timestamp"])
importance = pd.read_csv(IMPORTANCE_PATH)

best_model = comparison.iloc[0]

lot_summary = (
    pred.groupby("lot_id")
    .agg(
        wafer_count=("wafer_id", "size"),
        actual_defect_rate_percent=(
            "defect_flag",
            lambda s: s.mean() * 100.0,
        ),
        mean_raw_probability=("raw_probability", "mean"),
        mean_calibrated_probability=(
            "calibrated_probability",
            "mean",
        ),
        maximum_calibrated_probability=(
            "calibrated_probability",
            "max",
        ),
    )
    .reset_index()
)

high_risk = (
    pred.sort_values(
        "calibrated_probability",
        ascending=False,
    )
    .head(15)
)

summary = {
    "best_model": str(best_model["model"]),
    "best_average_precision": float(
        best_model["average_precision"]
    ),
    "best_roc_auc": float(best_model["roc_auc"]),
    "calibrated_brier_score": float(
        calibration.loc[
            calibration["model"]
            == "RandomForest_isotonic_calibrated",
            "brier_score",
        ].iloc[0]
    ),
    "top_permutation_feature": str(
        importance.iloc[0]["feature"]
    ),
}

JSON_OUTPUT.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

comparison_table = comparison.round(5).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
calibration_table = calibration.round(6).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
importance_table = importance.round(6).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
lot_table = lot_summary.round(5).to_html(
    index=False,
    border=0,
    classes="summary-table",
)
risk_table = high_risk.head(12).round(5).to_html(
    index=False,
    border=0,
    classes="summary-table",
)

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>앙상블 불량 예측 대시보드</title>
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
    font-size: 24px;
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
<h1>반도체 Physical AI 앙상블 불량 예측</h1>

<div class="kpi-grid">
  <div class="card">
    <div class="label">최고 모델</div>
    <div class="value">{summary["best_model"]}</div>
  </div>
  <div class="card">
    <div class="label">Best AP</div>
    <div class="value">{summary["best_average_precision"]:.3f}</div>
  </div>
  <div class="card">
    <div class="label">Best ROC-AUC</div>
    <div class="value">{summary["best_roc_auc"]:.3f}</div>
  </div>
  <div class="card">
    <div class="label">보정 Brier</div>
    <div class="value">{summary["calibrated_brier_score"]:.4f}</div>
  </div>
</div>

<div class="card">
  <h2>모델 비교</h2>
  {comparison_table}
</div>

<div class="card">
  <h2>확률 보정 비교</h2>
  {calibration_table}
</div>

<div class="card">
  <h2>Permutation Importance</h2>
  {importance_table}
</div>

<div class="card">
  <h2>Lot별 보정 불량확률</h2>
  {lot_table}
</div>

<div class="card">
  <h2>보정 위험 상위 Wafer</h2>
  {risk_table}
</div>

<div class="card note">
확률 보정은 예측확률의 해석 가능성을 개선할 수 있지만,
실제 폐기·정지·Recipe 변경 결정에는 독립 품질검증과 승인 절차가 필요합니다.
</div>
</body>
</html>
"""

HTML_OUTPUT.write_text(html, encoding="utf-8")

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] HTML: {HTML_OUTPUT}")
print(f"[완료] JSON: {JSON_OUTPUT}")
