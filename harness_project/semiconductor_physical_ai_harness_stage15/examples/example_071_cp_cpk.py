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
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "cp_cpk_summary.json"

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

metric = spec["metric"]
lsl = float(spec["lsl"])
usl = float(spec["usl"])
subgroup_size = int(spec["subgroup_size"])

# 1. 연속 subgroup_size개씩 부분군을 만든다.
df["subgroup_id"] = df.index // subgroup_size

# 2. 부분군 내부 표준편차의 평균으로 단기 변동을 추정한다.
subgroup_std = (
    df.groupby("subgroup_id")[metric]
    .std(ddof=1)
    .dropna()
)

within_sigma = float(subgroup_std.mean())
process_mean = float(df[metric].mean())

# 3. Cp와 Cpk를 계산한다.
cp = (usl - lsl) / (6.0 * within_sigma)

cpu = (usl - process_mean) / (3.0 * within_sigma)
cpl = (process_mean - lsl) / (3.0 * within_sigma)
cpk = min(cpu, cpl)

summary = {
    "metric": metric,
    "lsl": lsl,
    "usl": usl,
    "process_mean": process_mean,
    "within_sigma": within_sigma,
    "cp": cp,
    "cpu": cpu,
    "cpl": cpl,
    "cpk": cpk,
}

OUTPUT_PATH.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
