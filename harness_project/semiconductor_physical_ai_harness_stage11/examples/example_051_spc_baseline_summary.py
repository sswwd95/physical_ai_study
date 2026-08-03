"""
반도체 Physical AI 하네스 엔지니어링 실습 051~055
Windows 10 / Anaconda / Pandas / Matplotlib
SPC 관리도와 경보 규칙
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "temperature_spc_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "spc_baseline_summary.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 초기 200개 샘플을 안정 공정 기준 구간으로 사용한다.
baseline = df["temperature_c"].iloc[:200]

# 2. 평균과 표준편차를 계산한다.
mean_value = float(baseline.mean())
std_value = float(baseline.std(ddof=1))

# 3. 1σ, 2σ, 3σ 구간을 계산한다.
summary = {
    "baseline_rows": len(baseline),
    "mean": mean_value,
    "std": std_value,
    "lower_1sigma": mean_value - 1 * std_value,
    "upper_1sigma": mean_value + 1 * std_value,
    "lower_2sigma": mean_value - 2 * std_value,
    "upper_2sigma": mean_value + 2 * std_value,
    "lower_3sigma": mean_value - 3 * std_value,
    "upper_3sigma": mean_value + 3 * std_value,
}

# 4. 결과를 JSON으로 저장한다.
OUTPUT_PATH.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
