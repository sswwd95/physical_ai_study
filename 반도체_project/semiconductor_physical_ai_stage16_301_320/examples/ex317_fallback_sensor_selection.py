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

temp_a = sensor_df["temp_sensor_a_c"].interpolate(limit_direction="both")
temp_b = sensor_df["temp_sensor_b_c"].interpolate(limit_direction="both")

error_a = np.abs(temp_a - sensor_df["true_temperature_c"])
error_b = np.abs(temp_b - sensor_df["true_temperature_c"])

confidence_a = np.exp(-error_a / 1.5)
confidence_b = np.exp(-error_b / 1.5)

sensor_df["selected_sensor"] = np.where(
    confidence_a >= confidence_b,
    "temp_sensor_a",
    "temp_sensor_b",
)

sensor_df["selected_temperature_c"] = np.where(
    sensor_df["selected_sensor"] == "temp_sensor_a",
    temp_a,
    temp_b,
)

print(sensor_df["selected_sensor"].value_counts())
