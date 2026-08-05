from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

baseline = sensor_df["chamber_temp_c"].iloc[:120]
mu0 = baseline.mean()
sigma = baseline.std(ddof=1)

lambda_value = 0.2
l_value = 3.0

sensor_df["temp_ewma"] = (
    sensor_df["chamber_temp_c"]
    .ewm(alpha=lambda_value, adjust=False)
    .mean()
)

t = np.arange(1, len(sensor_df) + 1)
ewma_std = sigma * np.sqrt(
    lambda_value / (2 - lambda_value)
    * (1 - (1 - lambda_value) ** (2 * t))
)

sensor_df["ewma_ucl"] = mu0 + l_value * ewma_std
sensor_df["ewma_lcl"] = mu0 - l_value * ewma_std
sensor_df["ewma_alarm"] = (
    (sensor_df["temp_ewma"] > sensor_df["ewma_ucl"])
    | (sensor_df["temp_ewma"] < sensor_df["ewma_lcl"])
)

print("EWMA 경보 수:", int(sensor_df["ewma_alarm"].sum()))
sensor_df.to_csv(
    OUTPUT_DIR / "ex067_ewma_control_limits.csv",
    index=False,
    encoding="utf-8-sig",
)
