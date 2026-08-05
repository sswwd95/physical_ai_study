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

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])
sensor_df = sensor_df.sort_values("timestamp")

sensor_columns = [
    "temp_sensor_a_c",
    "temp_sensor_b_c",
    "pressure_sensor_a_pa",
    "pressure_sensor_b_pa",
    "rf_sensor_w",
    "gas_sensor_sccm",
]

before = sensor_df[sensor_columns].isna().sum()
sensor_df[sensor_columns] = sensor_df[sensor_columns].interpolate(
    method="linear",
    limit_direction="both",
)
after = sensor_df[sensor_columns].isna().sum()

summary_df = pd.DataFrame({
    "missing_before": before,
    "missing_after": after,
})
print(summary_df)
sensor_df.to_csv(
    OUTPUT_DIR / "ex303_interpolated_stream.csv",
    index=False,
    encoding="utf-8-sig",
)
