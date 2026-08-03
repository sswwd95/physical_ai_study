from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/digital_twin_sensor_stream.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE)

residual = (
    sensor_df["temp_sensor_b_c"]
    - sensor_df["true_temperature_c"]
)

rolling_mean = residual.rolling(60, min_periods=20).mean()
rolling_std = residual.rolling(60, min_periods=20).std()

upper = rolling_mean + 3 * rolling_std
lower = rolling_mean - 3 * rolling_std

sensor_df["dynamic_alarm"] = (
    (residual > upper)
    | (residual < lower)
)

print("동적 경보 수:", int(sensor_df["dynamic_alarm"].sum()))
sensor_df[
    ["timestamp", "temp_sensor_b_c", "true_temperature_c", "dynamic_alarm"]
].to_csv(
    OUTPUT_DIR / "ex315_dynamic_alarm.csv",
    index=False,
    encoding="utf-8-sig",
)
