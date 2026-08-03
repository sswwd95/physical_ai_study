"""
반도체 Physical AI 하네스 엔지니어링 실습 036~040
Windows 10 / Anaconda / Pandas / SciPy
센서 노이즈 분석과 필터링
"""

from pathlib import Path
import pandas as pd
from scipy.signal import savgol_filter

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "sensor_signal_noisy.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_savgol_filtered.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

window_length = 15
polyorder = 2
filtered = df.copy()

# 1. 센서별 Savitzky-Golay 필터를 적용한다.
for sensor in sensor_columns:
    filtered[f"{sensor}_savgol"] = savgol_filter(
        df[sensor].to_numpy(),
        window_length=window_length,
        polyorder=polyorder,
        mode="interp",
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
    f"window_length={window_length}, polyorder={polyorder}"
)
print(
    "Savitzky-Golay 필터는 곡선 형태를 비교적 "
    "보존하면서 노이즈를 줄입니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
