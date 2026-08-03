"""
반도체 Physical AI 하네스 엔지니어링 실습 081~085
Windows 10 / Anaconda / Pandas / SciPy
불량 라벨, 불량률, 교차표, 위험비 분석
"""

from pathlib import Path
import pandas as pd
from scipy.stats import chi2_contingency

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "wafer_process_quality.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "chi_square_crosstab_summary.csv"

df = pd.read_csv(INPUT_PATH)

categorical_columns = [
    "recipe_id",
    "tool_id",
]

rows = []

# 1. 범주형 조건과 불량 라벨의 교차표를 만든다.
for column in categorical_columns:
    table = pd.crosstab(
        df[column],
        df["defect_flag"],
    )

    # 2. 카이제곱 독립성 검정을 수행한다.
    chi2_stat, p_value, dof, expected = chi2_contingency(
        table
    )

    rows.append(
        {
            "condition": column,
            "category_count": int(table.shape[0]),
            "chi2_statistic": float(chi2_stat),
            "degrees_of_freedom": int(dof),
            "p_value": float(p_value),
            "association_detected_at_0_05": bool(
                p_value < 0.05
            ),
            "minimum_expected_count": float(
                expected.min()
            ),
        }
    )

result = pd.DataFrame(rows)
result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.round(6))
print()
print(
    "p-value<0.05는 연관성 근거이며 "
    "원인·인과관계의 확정이 아닙니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
