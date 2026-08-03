"""
반도체 Physical AI 하네스 엔지니어링 실습 056~060
Windows 10 / Anaconda / Pandas / Matplotlib
EWMA, CUSUM, 작은 평균 이동, 통합 공정 경보
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "temperature_shift_log.csv"
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "cusum_control_chart.csv"
PNG_OUTPUT = PROJECT_ROOT / "outputs" / "cusum_control_chart.png"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 초기 200개 샘플로 기준 평균과 표준편차를 계산한다.
baseline = df["temperature_c"].iloc[:200]
mu0 = float(baseline.mean())
sigma = float(baseline.std(ddof=1))

# 2. 표준화 CUSUM 파라미터를 정의한다.
k = 0.5
h = 5.0

positive_cusum = []
negative_cusum = []

c_plus = 0.0
c_minus = 0.0

# 3. 센서값을 표준화하고 양·음 CUSUM을 누적한다.
for value in df["temperature_c"]:
    z = (value - mu0) / sigma

    c_plus = max(
        0.0,
        c_plus + z - k,
    )

    c_minus = min(
        0.0,
        c_minus + z + k,
    )

    positive_cusum.append(c_plus)
    negative_cusum.append(c_minus)

result = df.copy()
result["cusum_positive"] = positive_cusum
result["cusum_negative"] = negative_cusum

# 4. 의사결정 한계 h를 넘으면 경보로 처리한다.
result["positive_alert"] = (
    result["cusum_positive"] > h
)

result["negative_alert"] = (
    result["cusum_negative"] < -h
)

result["cusum_alert"] = (
    result["positive_alert"]
    | result["negative_alert"]
)

result.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

# 5. CUSUM 관리도를 저장한다.
plt.figure(figsize=(12, 5))
plt.plot(
    result["timestamp"],
    result["cusum_positive"],
    label="C+",
)
plt.plot(
    result["timestamp"],
    result["cusum_negative"],
    label="C-",
)
plt.axhline(h, linestyle="--", label="+h")
plt.axhline(-h, linestyle="--", label="-h")
plt.axhline(0.0, linestyle="--", label="0")
plt.title("CUSUM Control Chart")
plt.xlabel("Timestamp")
plt.ylabel("Standardized CUSUM")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(PNG_OUTPUT, dpi=150)
plt.close()

print("CUSUM 경보 행 수:", int(result["cusum_alert"].sum()))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] PNG: {PNG_OUTPUT}")
