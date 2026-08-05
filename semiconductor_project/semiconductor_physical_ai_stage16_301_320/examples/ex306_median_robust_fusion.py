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

temp_values = sensor_df[
    ["temp_sensor_a_c", "temp_sensor_b_c", "true_temperature_c"]
].copy()

sensor_df["median_temperature_c"] = temp_values[
    ["temp_sensor_a_c", "temp_sensor_b_c"]
].median(axis=1, skipna=True)

absolute_error = np.abs(
    sensor_df["median_temperature_c"]
    - sensor_df["true_temperature_c"]
)

print("중앙값 융합 MAE:", round(absolute_error.mean(), 4))
