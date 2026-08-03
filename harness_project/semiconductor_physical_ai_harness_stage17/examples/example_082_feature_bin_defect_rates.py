"""
반도체 Physical AI 하네스 엔지니어링 실습 081~085
Windows 10 / Anaconda / Pandas / SciPy
불량 라벨, 불량률, 교차표, 위험비 분석
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "wafer_process_quality.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "feature_bin_defect_rates.csv"

df = pd.read_csv(INPUT_PATH)

features = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

rows = []

# 1. 각 센서를 4분위 구간으로 나눈다.
for feature in features:
    bin_column = f"{feature}_quartile"

    df[bin_column] = pd.qcut(
        df[feature],
        q=4,
        duplicates="drop",
    )

    # 2. 구간별 표본 수와 불량률을 계산한다.
    grouped = (
        df.groupby(
            bin_column,
            observed=False,
        )
        .agg(
            sample_count=("defect_flag", "size"),
            defect_count=("defect_flag", "sum"),
            defect_rate=("defect_flag", "mean"),
            feature_mean=(feature, "mean"),
        )
        .reset_index()
    )

    for _, row in grouped.iterrows():
        rows.append(
            {
                "feature": feature,
                "bin": str(row[bin_column]),
                "sample_count": int(row["sample_count"]),
                "defect_count": int(row["defect_count"]),
                "defect_rate_percent": float(
                    row["defect_rate"] * 100.0
                ),
                "feature_mean": float(row["feature_mean"]),
            }
        )

result = pd.DataFrame(rows)
result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.round(4))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
