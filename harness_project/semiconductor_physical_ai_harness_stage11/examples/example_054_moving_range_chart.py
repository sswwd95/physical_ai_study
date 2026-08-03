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
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "moving_range_chart.csv"
PNG_OUTPUT = PROJECT_ROOT / "outputs" / "moving_range_chart.png"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 연속 두 샘플의 절대 차이를 이동범위로 계산한다.
df["moving_range"] = df["temperature_c"].diff().abs()

# 2. 초기 200개 샘플 구간의 평균 이동범위를 계산한다.
baseline_mr = df["moving_range"].iloc[1:200]
mr_bar = float(baseline_mr.mean())

# n=2 이동범위 관리도의 D4 상수는 3.267이다.
ucl = 3.267 * mr_bar
lcl = 0.0

# 3. 이동범위 관리선을 추가한다.
df["mr_center_line"] = mr_bar
df["mr_ucl"] = ucl
df["mr_lcl"] = lcl
df["mr_out_of_control"] = df["moving_range"] > ucl

df.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

# 4. 이동범위 관리도를 저장한다.
plt.figure(figsize=(12, 5))
plt.plot(df["timestamp"], df["moving_range"], linewidth=0.9)
plt.axhline(mr_bar, linestyle="--", label="MR mean")
plt.axhline(ucl, linestyle="--", label="UCL")
plt.axhline(lcl, linestyle="--", label="LCL")
plt.title("Moving Range Chart")
plt.xlabel("Timestamp")
plt.ylabel("Moving Range")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(PNG_OUTPUT, dpi=150)
plt.close()

print("이동범위 위반 행 수:", int(df["mr_out_of_control"].sum()))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] PNG: {PNG_OUTPUT}")
