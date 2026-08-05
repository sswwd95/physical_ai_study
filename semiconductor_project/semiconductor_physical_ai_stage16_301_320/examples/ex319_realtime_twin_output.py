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

temp_a = sensor_df["temp_sensor_a_c"].interpolate(limit_direction="both")
temp_b = sensor_df["temp_sensor_b_c"].interpolate(limit_direction="both")
pressure_a = sensor_df["pressure_sensor_a_pa"].interpolate(limit_direction="both")
pressure_b = sensor_df["pressure_sensor_b_pa"].interpolate(limit_direction="both")

sensor_df["fused_temperature_c"] = (
    0.7 * temp_a + 0.3 * temp_b
)
sensor_df["fused_pressure_pa"] = (
    0.75 * pressure_a + 0.25 * pressure_b
)

sensor_df["temperature_error"] = (
    sensor_df["fused_temperature_c"]
    - sensor_df["true_temperature_c"]
)
sensor_df["pressure_error"] = (
    sensor_df["fused_pressure_pa"]
    - sensor_df["true_pressure_pa"]
)

sensor_df["alarm"] = (
    sensor_df["temperature_error"].abs() > 2.0
) | (
    sensor_df["pressure_error"].abs() > 0.8
)

output_columns = [
    "timestamp",
    "process_phase",
    "fused_temperature_c",
    "fused_pressure_pa",
    "rf_sensor_w",
    "gas_sensor_sccm",
    "temperature_error",
    "pressure_error",
    "alarm",
]

sensor_df[output_columns].to_csv(
    OUTPUT_DIR / "ex319_realtime_twin_output.csv",
    index=False,
    encoding="utf-8-sig",
)

print(sensor_df[output_columns].head(10).round(4))
