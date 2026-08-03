"""
반도체 Physical AI 하네스 엔지니어링 실습 011~015
Windows 10 / Anaconda / Pandas / PyMC 연계 준비
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "rolling_sensor_statistics.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

# 1. 30초 이동창을 사용한다.
window_size = 30

# 2. 온도의 이동평균과 이동표준편차를 계산한다.
df["temperature_ma30"] = (
    df["temperature_c"]
    .rolling(window=window_size, min_periods=5)
    .mean()
)

df["temperature_std30"] = (
    df["temperature_c"]
    .rolling(window=window_size, min_periods=5)
    .std()
)

# 3. 진동과 전류의 이동평균도 계산한다.
df["vibration_ma30"] = (
    df["vibration_rms"]
    .rolling(window=window_size, min_periods=5)
    .mean()
)

df["current_ma30"] = (
    df["motor_current_a"]
    .rolling(window=window_size, min_periods=5)
    .mean()
)

# 4. 원시값과 이동평균의 차이를 잔차로 만든다.
df["temperature_residual"] = (
    df["temperature_c"] - df["temperature_ma30"]
)

# 5. 결과를 저장한다.
selected_columns = [
    "timestamp",
    "lot_id",
    "temperature_c",
    "temperature_ma30",
    "temperature_std30",
    "temperature_residual",
    "vibration_rms",
    "vibration_ma30",
    "motor_current_a",
    "current_ma30",
]

df[selected_columns].to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(df[selected_columns].tail(10).round(4))
print(f"[완료] 이동 통계 저장: {OUTPUT_PATH}")
