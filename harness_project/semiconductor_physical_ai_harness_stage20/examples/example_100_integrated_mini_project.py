"""
반도체 Physical AI 하네스 엔지니어링 실습 096~100
Windows 10 / Anaconda / Pandas / scikit-learn
불균형 데이터 처리와 001~100 통합 미니 프로젝트
"""

from pathlib import Path
import json
import joblib
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "imbalanced_wafer_quality.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "selected_cost_sensitive_model.joblib"
CLASS_PATH = PROJECT_ROOT / "outputs" / "class_balance_summary.json"
COST_PATH = PROJECT_ROOT / "outputs" / "cost_sensitive_model_comparison.csv"
HTML_OUTPUT = PROJECT_ROOT / "outputs" / "integrated_mini_project_dashboard.html"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "integrated_mini_project_summary.json"
PREDICTION_OUTPUT = PROJECT_ROOT / "outputs" / "integrated_mini_project_predictions.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

split_index = int(len(df) * 0.70)
test_df = df.iloc[split_index:].copy()

feature_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
    "recipe_id",
    "tool_id",
]

model = joblib.load(MODEL_PATH)
class_summary = json.loads(
    CLASS_PATH.read_text(encoding="utf-8")
)
cost_result = pd.read_csv(COST_PATH)

probability = model.predict_proba(
    test_df[feature_columns]
)[:, 1]

prediction = (probability >= 0.5).astype(int)

result = test_df[
    [
        "timestamp",
        "wafer_id",
        "lot_id",
        "recipe_id",
        "tool_id",
        "defect_flag",
    ]
].copy()

result["defect_probability"] = probability
result["predicted_defect"] = prediction

result.to_csv(
    PREDICTION_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

lot_summary = (
    result.groupby("lot_id")
    .agg(
        wafer_count=("wafer_id", "size"),
        actual_defect_rate_percent=(
            "defect_flag",
            lambda s: s.mean() * 100.0,
        ),
        predicted_defect_rate_percent=(
            "predicted_defect",
            lambda s: s.mean() * 100.0,
        ),
        mean_defect_probability=("defect_probability", "mean"),
        maximum_defect_probability=("defect_probability", "max"),
    )
    .reset_index()
)

high_risk = (
    result.sort_values(
        "defect_probability",
        ascending=False,
    )
    .head(20)
)

selected_row = cost_result.loc[
    cost_result["selected"]
].iloc[0]

summary = {
    "exercise_range": "001-100",
    "test_rows": len(result),
    "original_defect_rate_percent": float(
        class_summary["defect_rate_percent"]
    ),
    "selected_cost_sensitive_setting": str(
        selected_row["setting"]
    ),
    "selected_recall": float(
        selected_row["recall"]
    ),
    "selected_precision": float(
        selected_row["precision"]
    ),
    "selected_average_precision": float(
        selected_row["average_precision"]
    ),
    "selected_weighted_cost": int(
        selected_row["weighted_cost"]
    ),
}

JSON_OUTPUT.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

lot_table = lot_summary.round(5).to_html(
    index=False,
    border=0,
    classes="summary-table",
)

risk_table = high_risk.round(5).to_html(
    index=False,
    border=0,
    classes="summary-table",
)

cost_table = cost_result.round(5).to_html(
    index=False,
    border=0,
    classes="summary-table",
)

html = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>반도체 Physical AI 001~100 통합 미니 프로젝트</title>
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
<h1>반도체 Physical AI 하네스 001~100 통합 미니 프로젝트</h1>

<div class="kpi-grid">
  <div class="card">
    <div class="label">원본 불량률</div>
    <div class="value">{summary["original_defect_rate_percent"]:.2f}%</div>
  </div>
  <div class="card">
    <div class="label">선택 설정</div>
    <div class="value">{summary["selected_cost_sensitive_setting"]}</div>
  </div>
  <div class="card">
    <div class="label">Recall</div>
    <div class="value">{summary["selected_recall"]:.3f}</div>
  </div>
  <div class="card">
    <div class="label">Average Precision</div>
    <div class="value">{summary["selected_average_precision"]:.3f}</div>
  </div>
</div>

<div class="card">
  <h2>비용 민감 모델 비교</h2>
  {cost_table}
</div>

<div class="card">
  <h2>Lot별 실제·예측 불량 위험</h2>
  {lot_table}
</div>

<div class="card">
  <h2>고위험 Wafer</h2>
  {risk_table}
</div>

<div class="card note">
본 미니 프로젝트는 001~100 실습의 데이터 품질, 전처리, SPC, 공정 능력,
불량 분석, 머신러닝 모델링 흐름을 연결하는 교육용 예제입니다.
실제 장비 정지·Wafer 폐기·Recipe 변경 결정에는 별도 검증과 승인 절차가 필요합니다.
</div>
</body>
</html>
"""

HTML_OUTPUT.write_text(
    html,
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] 예측: {PREDICTION_OUTPUT}")
print(f"[완료] HTML: {HTML_OUTPUT}")
print(f"[완료] JSON: {JSON_OUTPUT}")
