"""
반도체 Physical AI 하네스 엔지니어링 실습 051~055
Windows 10 / Anaconda / Pandas / Matplotlib
SPC 관리도와 경보 규칙
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "temperature_spc_log.csv"
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "individuals_control_chart.csv"
PNG_OUTPUT = PROJECT_ROOT / "outputs" / "individuals_control_chart.png"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 초기 200개 샘플을 기준 구간으로 사용한다.
baseline = df["temperature_c"].iloc[:200]

center_line = float(baseline.mean())
std_value = float(baseline.std(ddof=1))

ucl = center_line + 3.0 * std_value
lcl = center_line - 3.0 * std_value

# 2. 개별값 관리선과 위반 여부를 계산한다.
result = df.copy()
result["center_line"] = center_line
result["ucl"] = ucl
result["lcl"] = lcl
result["out_of_control"] = (
    (result["temperature_c"] > ucl)
    | (result["temperature_c"] < lcl)
)

result.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

# 3. 개별값 관리도를 저장한다.
plt.figure(figsize=(12, 5))
plt.plot(
    result["timestamp"],
    result["temperature_c"],
    linewidth=0.9,
)
plt.axhline(center_line, linestyle="--", label="CL")
plt.axhline(ucl, linestyle="--", label="UCL")
plt.axhline(lcl, linestyle="--", label="LCL")
plt.title("Individuals Control Chart")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(PNG_OUTPUT, dpi=150)
plt.close()

print("관리한계 위반 행 수:", int(result["out_of_control"].sum()))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] PNG: {PNG_OUTPUT}")
