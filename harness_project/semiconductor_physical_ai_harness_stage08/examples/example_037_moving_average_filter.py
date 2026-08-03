"""
반도체 Physical AI 하네스 엔지니어링 실습 036~040
Windows 10 / Anaconda / Pandas / SciPy
센서 노이즈 분석과 필터링
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "sensor_signal_noisy.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_moving_average.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

window_size = 11
filtered = df.copy()

# 1. 센서별 중심 이동평균을 계산한다.
for sensor in sensor_columns:
    filtered[f"{sensor}_ma11"] = (
        df[sensor]
        .rolling(
            window=window_size,
            center=True,
            min_periods=1,
        )
        .mean()
    )

# 2. 결과를 저장한다.
filtered.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(filtered.head(15).round(4))
print()
print(
    "주의: 이동평균은 노이즈를 줄이지만 "
    "빠른 변화와 피크를 둔화시킬 수 있습니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
