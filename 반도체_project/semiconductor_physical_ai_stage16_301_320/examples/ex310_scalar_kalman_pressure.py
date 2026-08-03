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

measurement = (
    sensor_df["pressure_sensor_a_pa"]
    .interpolate(limit_direction="both")
    .to_numpy()
)

process_variance = 0.01
measurement_variance = 0.18 ** 2

estimate = measurement[0]
estimate_variance = 1.0
filtered = []

for value in measurement:
    estimate_variance += process_variance
    kalman_gain = (
        estimate_variance
        / (estimate_variance + measurement_variance)
    )
    estimate = estimate + kalman_gain * (value - estimate)
    estimate_variance = (
        1 - kalman_gain
    ) * estimate_variance
    filtered.append(estimate)

sensor_df["kalman_pressure_pa"] = filtered

rmse = np.sqrt(
    np.mean(
        (
            sensor_df["kalman_pressure_pa"]
            - sensor_df["true_pressure_pa"]
        ) ** 2
    )
)

print("Kalman 압력 RMSE:", round(rmse, 4))
