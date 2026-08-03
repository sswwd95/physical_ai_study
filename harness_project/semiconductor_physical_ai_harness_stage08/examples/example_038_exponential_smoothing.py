"""
반도체 Physical AI 하네스 엔지니어링 실습 036~040
Windows 10 / Anaconda / Pandas / SciPy
센서 노이즈 분석과 필터링
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "sensor_signal_noisy.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_exponential_smoothing.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

alpha = 0.20
smoothed = df.copy()

# 1. 센서별 지수이동평균을 계산한다.
for sensor in sensor_columns:
    smoothed[f"{sensor}_ewm"] = (
        df[sensor]
        .ewm(
            alpha=alpha,
            adjust=False,
        )
        .mean()
    )

# 2. 결과를 저장한다.
smoothed.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(smoothed.head(15).round(4))
print()
print(
    f"alpha={alpha}: 값이 작을수록 더 부드럽지만 "
    "반응이 느려집니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
