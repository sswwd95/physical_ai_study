"""
반도체 Physical AI 하네스 엔지니어링 실습 081~085
Windows 10 / Anaconda / Pandas / SciPy
불량 라벨, 불량률, 교차표, 위험비 분석
"""

from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "wafer_process_quality.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "condition_risk_ratios.csv"

df = pd.read_csv(INPUT_PATH)

# 1. 분석할 이진 노출 조건을 정의한다.
conditions = {
    "recipe_rcp03": df["recipe_id"] == "RCP_03",
    "tool_c": df["tool_id"] == "TOOL_C",
    "temperature_high": df["temperature_c"] >= 65.5,
    "vibration_high": df["vibration_rms"] >= 2.0,
    "current_high": df["motor_current_a"] >= 8.3,
}

rows = []

# 2. 각 조건의 노출·비노출 불량 위험과 위험비를 계산한다.
for condition_name, exposed in conditions.items():
    unexposed = ~exposed

    exposed_total = int(exposed.sum())
    unexposed_total = int(unexposed.sum())

    exposed_defects = int(
        df.loc[exposed, "defect_flag"].sum()
    )
    unexposed_defects = int(
        df.loc[unexposed, "defect_flag"].sum()
    )

    exposed_risk = exposed_defects / exposed_total
    unexposed_risk = unexposed_defects / unexposed_total

    risk_ratio = (
        exposed_risk / unexposed_risk
        if unexposed_risk > 0
        else np.nan
    )

    risk_difference = exposed_risk - unexposed_risk

    rows.append(
        {
            "condition": condition_name,
            "exposed_total": exposed_total,
            "unexposed_total": unexposed_total,
            "exposed_defects": exposed_defects,
            "unexposed_defects": unexposed_defects,
            "exposed_risk_percent": exposed_risk * 100.0,
            "unexposed_risk_percent": unexposed_risk * 100.0,
            "risk_ratio": risk_ratio,
            "risk_difference_percentage_points": (
                risk_difference * 100.0
            ),
        }
    )

result = pd.DataFrame(rows)
result = result.sort_values(
    "risk_ratio",
    ascending=False,
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.round(4))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
