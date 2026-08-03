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
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "spec_violation_rows.csv"
SUMMARY_PATH = PROJECT_ROOT / "outputs" / "spec_violation_summary.json"

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

metric = spec["metric"]
lsl = float(spec["lsl"])
usl = float(spec["usl"])

# 1. 하한·상한 규격 위반을 구분한다.
df["below_lsl"] = df[metric] < lsl
df["above_usl"] = df[metric] > usl
df["out_of_spec"] = df["below_lsl"] | df["above_usl"]

violations = df.loc[df["out_of_spec"]].copy()
violations.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

summary = {
    "total_rows": len(df),
    "below_lsl_count": int(df["below_lsl"].sum()),
    "above_usl_count": int(df["above_usl"].sum()),
    "out_of_spec_count": int(df["out_of_spec"].sum()),
    "out_of_spec_rate_percent": float(df["out_of_spec"].mean() * 100.0),
    "ppm_observed": float(df["out_of_spec"].mean() * 1_000_000.0),
}

SUMMARY_PATH.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] 위반 행: {OUTPUT_PATH}")
print(f"[완료] 요약: {SUMMARY_PATH}")
