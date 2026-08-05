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

temp_error = np.abs(
    sensor_df["temp_sensor_b_c"]
    - sensor_df["true_temperature_c"]
)

missing_penalty = (
    sensor_df["temp_sensor_b_c"].isna().astype(float)
)

sensor_df["temp_sensor_confidence"] = np.exp(
    -temp_error / 2.0
) * (1 - 0.8 * missing_penalty)

print(
    sensor_df["temp_sensor_confidence"].describe().round(4)
)
