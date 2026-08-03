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
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "xbar_control_chart.csv"
PNG_OUTPUT = PROJECT_ROOT / "outputs" / "xbar_control_chart.png"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

subgroup_size = 5

# 1. 5개 샘플씩 부분군 번호를 만든다.
df["subgroup_id"] = df.index // subgroup_size

# 2. 부분군별 평균을 계산한다.
subgroup = (
    df.groupby("subgroup_id")
    .agg(
        start_time=("timestamp", "min"),
        end_time=("timestamp", "max"),
        xbar=("temperature_c", "mean"),
        subgroup_std=("temperature_c", "std"),
        sample_count=("temperature_c", "size"),
    )
    .reset_index()
)

# 3. 초기 40개 부분군을 기준 구간으로 사용한다.
baseline = subgroup.iloc[:40]

center_line = float(baseline["xbar"].mean())
sigma_xbar = float(baseline["xbar"].std(ddof=1))

ucl = center_line + 3.0 * sigma_xbar
lcl = center_line - 3.0 * sigma_xbar

# 4. 관리선과 위반 여부를 추가한다.
subgroup["center_line"] = center_line
subgroup["ucl"] = ucl
subgroup["lcl"] = lcl
subgroup["out_of_control"] = (
    (subgroup["xbar"] > ucl)
    | (subgroup["xbar"] < lcl)
)

subgroup.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

# 5. X-bar 관리도를 저장한다.
plt.figure(figsize=(12, 5))
plt.plot(subgroup["subgroup_id"], subgroup["xbar"], marker="o", markersize=3)
plt.axhline(center_line, linestyle="--", label="CL")
plt.axhline(ucl, linestyle="--", label="UCL")
plt.axhline(lcl, linestyle="--", label="LCL")
plt.title("X-bar Control Chart")
plt.xlabel("Subgroup ID")
plt.ylabel("Mean Temperature (°C)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(PNG_OUTPUT, dpi=150)
plt.close()

print(subgroup.loc[subgroup["out_of_control"]].head(20))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] PNG: {PNG_OUTPUT}")
