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
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "pp_ppk_summary.json"

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

metric = spec["metric"]
lsl = float(spec["lsl"])
usl = float(spec["usl"])

# 1. 전체 기간 표준편차를 장기 변동으로 사용한다.
overall_sigma = float(df[metric].std(ddof=1))
process_mean = float(df[metric].mean())

# 2. Pp와 Ppk를 계산한다.
pp = (usl - lsl) / (6.0 * overall_sigma)

ppu = (usl - process_mean) / (3.0 * overall_sigma)
ppl = (process_mean - lsl) / (3.0 * overall_sigma)
ppk = min(ppu, ppl)

summary = {
    "metric": metric,
    "lsl": lsl,
    "usl": usl,
    "process_mean": process_mean,
    "overall_sigma": overall_sigma,
    "pp": pp,
    "ppu": ppu,
    "ppl": ppl,
    "ppk": ppk,
}

OUTPUT_PATH.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
