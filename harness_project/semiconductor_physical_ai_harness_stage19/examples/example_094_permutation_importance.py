"""
반도체 Physical AI 하네스 엔지니어링 실습 091~095
Windows 10 / Anaconda / Pandas / scikit-learn
Decision Tree, Random Forest, 확률 보정, 특징 중요도
"""

from pathlib import Path
import joblib
import pandas as pd
from sklearn.inspection import permutation_importance

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEST_PATH = PROJECT_ROOT / "outputs" / "test_tree_data.csv"
RF_PATH = PROJECT_ROOT / "models" / "random_forest_model.joblib"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "random_forest_permutation_importance.csv"

test_df = pd.read_csv(TEST_PATH, parse_dates=["timestamp"])
model = joblib.load(RF_PATH)

feature_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
    "recipe_id",
    "tool_id",
]

# 1. 테스트 데이터에서 Average Precision 감소량으로 중요도를 계산한다.
result = permutation_importance(
    model,
    test_df[feature_columns],
    test_df["defect_flag"],
    scoring="average_precision",
    n_repeats=20,
    random_state=42,
    n_jobs=-1,
)

importance_df = pd.DataFrame({
    "feature": feature_columns,
    "importance_mean": result.importances_mean,
    "importance_std": result.importances_std,
})

importance_df["importance_positive"] = (
    importance_df["importance_mean"] > 0
)

importance_df = importance_df.sort_values(
    "importance_mean",
    ascending=False,
).reset_index(drop=True)

importance_df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(importance_df.round(6))
print()
print(
    "Permutation Importance는 해당 특징을 섞었을 때 "
    "평가 성능이 얼마나 감소하는지 측정합니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
