"""
반도체 Physical AI 하네스 엔지니어링 실습 076~080
Windows 10 / Anaconda / Pandas / SciPy
공정 능력 불확실성과 비정규 분포
"""

from pathlib import Path
import json
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "capability_uncertainty_log.csv"
SPEC_PATH = PROJECT_ROOT / "data" / "capability_specs.json"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "nonnormal_capability_summary.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
specs = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

rows = []

for metric, spec in specs.items():
    values = df[metric].dropna().to_numpy()
    lsl = float(spec["lsl"])
    usl = float(spec["usl"])

    # 1. 정규 가정 기반 Ppk를 계산한다.
    mean_value = float(np.mean(values))
    sigma = float(np.std(values, ddof=1))
    ppk_normal = min(
        (usl - mean_value) / (3.0 * sigma),
        (mean_value - lsl) / (3.0 * sigma),
    )

    # 2. 비정규 공정은 0.135%, 50%, 99.865% 분위수를 사용한다.
    q_low, q_median, q_high = np.quantile(
        values,
        [0.00135, 0.5, 0.99865],
    )

    upper_spread = q_high - q_median
    lower_spread = q_median - q_low

    cpu_percentile = (
        (usl - q_median) / upper_spread
        if upper_spread > 0
        else np.nan
    )
    cpl_percentile = (
        (q_median - lsl) / lower_spread
        if lower_spread > 0
        else np.nan
    )

    ppk_percentile = float(
        min(cpu_percentile, cpl_percentile)
    )

    rows.append(
        {
            "metric": metric,
            "mean": mean_value,
            "median": float(q_median),
            "std": sigma,
            "ppk_normal_assumption": float(ppk_normal),
            "q_0_135_percent": float(q_low),
            "q_99_865_percent": float(q_high),
            "ppk_percentile_method": ppk_percentile,
        }
    )

result = pd.DataFrame(rows)
result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.round(5))
print()
print("비정규 데이터에서는 정규 가정 지수와 분위수 지수를 함께 비교합니다.")
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
