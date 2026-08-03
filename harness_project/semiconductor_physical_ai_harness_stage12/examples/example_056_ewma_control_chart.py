"""
반도체 Physical AI 하네스 엔지니어링 실습 056~060
Windows 10 / Anaconda / Pandas / Matplotlib
EWMA, CUSUM, 작은 평균 이동, 통합 공정 경보
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "temperature_shift_log.csv"
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "ewma_control_chart.csv"
PNG_OUTPUT = PROJECT_ROOT / "outputs" / "ewma_control_chart.png"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 초기 200개 샘플을 안정 기준 구간으로 사용한다.
baseline = df["temperature_c"].iloc[:200]
mu0 = float(baseline.mean())
sigma = float(baseline.std(ddof=1))

# 2. EWMA 파라미터를 정의한다.
lambda_value = 0.20
L = 3.0

# 3. EWMA 값을 재귀적으로 계산한다.
ewma_values = []
previous = mu0

for value in df["temperature_c"]:
    current = (
        lambda_value * value
        + (1.0 - lambda_value) * previous
    )
    ewma_values.append(current)
    previous = current

result = df.copy()
result["ewma"] = ewma_values

# 4. 시간에 따라 변화하는 EWMA 관리한계를 계산한다.
time_index = np.arange(1, len(result) + 1)

ewma_sigma = sigma * np.sqrt(
    lambda_value
    / (2.0 - lambda_value)
    * (
        1.0
        - (1.0 - lambda_value) ** (2 * time_index)
    )
)

result["center_line"] = mu0
result["ucl"] = mu0 + L * ewma_sigma
result["lcl"] = mu0 - L * ewma_sigma

result["ewma_alert"] = (
    (result["ewma"] > result["ucl"])
    | (result["ewma"] < result["lcl"])
)

result.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

# 5. EWMA 관리도를 저장한다.
plt.figure(figsize=(12, 5))
plt.plot(result["timestamp"], result["ewma"], label="EWMA")
plt.plot(result["timestamp"], result["ucl"], linestyle="--", label="UCL")
plt.plot(result["timestamp"], result["lcl"], linestyle="--", label="LCL")
plt.axhline(mu0, linestyle="--", label="CL")
plt.title("EWMA Control Chart")
plt.xlabel("Timestamp")
plt.ylabel("EWMA Temperature (°C)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig(PNG_OUTPUT, dpi=150)
plt.close()

print("EWMA 경보 행 수:", int(result["ewma_alert"].sum()))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] PNG: {PNG_OUTPUT}")
