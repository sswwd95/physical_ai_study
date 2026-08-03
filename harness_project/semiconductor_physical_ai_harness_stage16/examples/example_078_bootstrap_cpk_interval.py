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
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "bootstrap_cpk_intervals.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
specs = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

rng = np.random.default_rng(42)
bootstrap_samples = 2000

def calculate_cpk(values, lsl, usl):
    mean_value = float(np.mean(values))
    sigma = float(np.std(values, ddof=1))

    if sigma <= 0:
        return np.nan

    return min(
        (usl - mean_value) / (3.0 * sigma),
        (mean_value - lsl) / (3.0 * sigma),
    )

rows = []

for metric, spec in specs.items():
    values = df[metric].dropna().to_numpy()
    lsl = float(spec["lsl"])
    usl = float(spec["usl"])

    observed_cpk = calculate_cpk(values, lsl, usl)

    bootstrap_cpks = []

    for _ in range(bootstrap_samples):
        sample = rng.choice(
            values,
            size=len(values),
            replace=True,
        )
        bootstrap_cpks.append(
            calculate_cpk(sample, lsl, usl)
        )

    bootstrap_cpks = np.asarray(bootstrap_cpks)
    bootstrap_cpks = bootstrap_cpks[
        np.isfinite(bootstrap_cpks)
    ]

    lower, upper = np.quantile(
        bootstrap_cpks,
        [0.025, 0.975],
    )

    rows.append(
        {
            "metric": metric,
            "observed_cpk": float(observed_cpk),
            "bootstrap_samples": len(bootstrap_cpks),
            "cpk_ci_2_5_percent": float(lower),
            "cpk_ci_97_5_percent": float(upper),
            "interval_width": float(upper - lower),
        }
    )

result = pd.DataFrame(rows)
result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.round(5))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
