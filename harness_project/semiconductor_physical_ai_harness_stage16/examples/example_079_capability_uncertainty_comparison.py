"""
반도체 Physical AI 하네스 엔지니어링 실습 076~080
Windows 10 / Anaconda / Pandas / SciPy
공정 능력 불확실성과 비정규 분포
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
NORMALITY_PATH = PROJECT_ROOT / "outputs" / "normality_test_summary.csv"
NONNORMAL_PATH = PROJECT_ROOT / "outputs" / "nonnormal_capability_summary.csv"
BOOTSTRAP_PATH = PROJECT_ROOT / "outputs" / "bootstrap_cpk_intervals.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "capability_uncertainty_comparison.csv"

normality = pd.read_csv(NORMALITY_PATH)
nonnormal = pd.read_csv(NONNORMAL_PATH)
bootstrap = pd.read_csv(BOOTSTRAP_PATH)

# 1. 세 분석 결과를 metric 기준으로 결합한다.
result = (
    normality.merge(
        nonnormal,
        on="metric",
        how="inner",
    )
    .merge(
        bootstrap,
        on="metric",
        how="inner",
    )
)

# 2. 정규성 결과에 따라 권장 지수를 선택한다.
def select_recommended_index(row):
    if row["normality_rejected_at_0_05"]:
        return row["ppk_percentile_method"]
    return row["ppk_normal_assumption"]

result["recommended_capability_index"] = result.apply(
    select_recommended_index,
    axis=1,
)

result["recommended_method"] = result[
    "normality_rejected_at_0_05"
].map(
    {
        True: "percentile_method",
        False: "normal_assumption",
    }
)

# 3. Bootstrap 하한이 1.0 이상인지 보수적으로 확인한다.
result["bootstrap_lower_bound_above_1"] = (
    result["cpk_ci_2_5_percent"] >= 1.0
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(
    result[
        [
            "metric",
            "normality_rejected_at_0_05",
            "recommended_method",
            "recommended_capability_index",
            "observed_cpk",
            "cpk_ci_2_5_percent",
            "cpk_ci_97_5_percent",
            "bootstrap_lower_bound_above_1",
        ]
    ].round(5)
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
