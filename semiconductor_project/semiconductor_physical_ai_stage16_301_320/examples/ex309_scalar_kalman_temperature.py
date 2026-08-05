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
    sensor_df["temp_sensor_a_c"]
    .interpolate(limit_direction="both")
    .to_numpy()
)

process_variance = 0.02
measurement_variance = 0.45 ** 2

estimate = measurement[0]
estimate_variance = 1.0
filtered = []

for value in measurement:
    estimate_variance = estimate_variance + process_variance

    kalman_gain = (
        estimate_variance
        / (estimate_variance + measurement_variance)
    )

    estimate = estimate + kalman_gain * (value - estimate)
    estimate_variance = (
        1 - kalman_gain
    ) * estimate_variance

    filtered.append(estimate)

sensor_df["kalman_temperature_c"] = filtered

rmse = np.sqrt(
    np.mean(
        (
            sensor_df["kalman_temperature_c"]
            - sensor_df["true_temperature_c"]
        ) ** 2
    )
)

print("Kalman 온도 RMSE:", round(rmse, 4))
sensor_df[
    ["timestamp", "true_temperature_c", "kalman_temperature_c"]
].to_csv(
    OUTPUT_DIR / "ex309_kalman_temperature.csv",
    index=False,
    encoding="utf-8-sig",
)
