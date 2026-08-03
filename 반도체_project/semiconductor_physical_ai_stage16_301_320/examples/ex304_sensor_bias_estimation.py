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

temp_bias = (
    sensor_df["temp_sensor_b_c"] - sensor_df["temp_sensor_a_c"]
)
pressure_bias = (
    sensor_df["pressure_sensor_b_pa"]
    - sensor_df["pressure_sensor_a_pa"]
)

result_df = pd.DataFrame([
    {
        "sensor_pair": "temperature_b_minus_a",
        "mean_bias": temp_bias.mean(),
        "std_bias": temp_bias.std(),
    },
    {
        "sensor_pair": "pressure_b_minus_a",
        "mean_bias": pressure_bias.mean(),
        "std_bias": pressure_bias.std(),
    },
])

print(result_df.round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex304_sensor_bias.csv",
    index=False,
    encoding="utf-8-sig",
)
