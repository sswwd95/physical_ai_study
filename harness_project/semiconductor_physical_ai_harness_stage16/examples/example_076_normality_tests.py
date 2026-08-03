"""
반도체 Physical AI 하네스 엔지니어링 실습 076~080
Windows 10 / Anaconda / Pandas / SciPy
공정 능력 불확실성과 비정규 분포
"""

from pathlib import Path
import pandas as pd
from scipy.stats import normaltest, shapiro, skew, kurtosis

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "capability_uncertainty_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "normality_test_summary.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

metrics = [
    "temperature_c",
    "film_thickness_nm",
]

rows = []

for metric in metrics:
    values = df[metric].dropna()

    # 1. Shapiro-Wilk 검정은 최대 5000개 이하 표본에 사용한다.
    shapiro_stat, shapiro_p = shapiro(values)

    # 2. D'Agostino K² 검정으로 왜도와 첨도를 함께 평가한다.
    k2_stat, k2_p = normaltest(values)

    rows.append(
        {
            "metric": metric,
            "sample_count": len(values),
            "skewness": float(skew(values, bias=False)),
            "excess_kurtosis": float(kurtosis(values, fisher=True, bias=False)),
            "shapiro_statistic": float(shapiro_stat),
            "shapiro_p_value": float(shapiro_p),
            "dagostino_k2": float(k2_stat),
            "dagostino_p_value": float(k2_p),
            "normality_rejected_at_0_05": bool(
                shapiro_p < 0.05 or k2_p < 0.05
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
print("p-value가 0.05보다 작으면 정규성을 기각하는 근거가 됩니다.")
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
