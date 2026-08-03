"""
반도체 Physical AI 하네스 엔지니어링 실습 071~075
Windows 10 / Anaconda / Pandas / Matplotlib
공정 능력지수와 규격 이탈 분석
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "process_capability_temperature.csv"
SPEC_PATH = PROJECT_ROOT / "data" / "temperature_spec.json"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "lot_capability_comparison.csv"

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

metric = spec["metric"]
lsl = float(spec["lsl"])
usl = float(spec["usl"])
subgroup_size = int(spec["subgroup_size"])

rows = []

# 1. Lot별로 공정 능력지수를 계산한다.
for lot_id, lot_df in df.groupby("lot_id"):
    lot_df = lot_df.reset_index(drop=True).copy()
    lot_df["subgroup_id"] = lot_df.index // subgroup_size

    within_sigma = float(
        lot_df.groupby("subgroup_id")[metric]
        .std(ddof=1)
        .dropna()
        .mean()
    )

    overall_sigma = float(lot_df[metric].std(ddof=1))
    mean_value = float(lot_df[metric].mean())

    cp = (usl - lsl) / (6.0 * within_sigma)
    cpk = min(
        (usl - mean_value) / (3.0 * within_sigma),
        (mean_value - lsl) / (3.0 * within_sigma),
    )

    pp = (usl - lsl) / (6.0 * overall_sigma)
    ppk = min(
        (usl - mean_value) / (3.0 * overall_sigma),
        (mean_value - lsl) / (3.0 * overall_sigma),
    )

    out_of_spec_rate = float(
        (~lot_df[metric].between(lsl, usl))
        .mean()
        * 100.0
    )

    rows.append({
        "lot_id": lot_id,
        "recipe_id": lot_df["recipe_id"].iloc[0],
        "row_count": len(lot_df),
        "mean": mean_value,
        "within_sigma": within_sigma,
        "overall_sigma": overall_sigma,
        "cp": cp,
        "cpk": cpk,
        "pp": pp,
        "ppk": ppk,
        "out_of_spec_rate_percent": out_of_spec_rate,
    })

result = pd.DataFrame(rows)
result = result.sort_values(
    "cpk",
    ascending=False,
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.round(4))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
