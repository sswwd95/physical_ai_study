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

sensor_df["temp_b_residual"] = (
    sensor_df["temp_sensor_b_c"]
    - sensor_df["true_temperature_c"]
)
sensor_df["pressure_b_residual"] = (
    sensor_df["pressure_sensor_b_pa"]
    - sensor_df["true_pressure_pa"]
)

sensor_df["temp_sensor_fault"] = (
    sensor_df["temp_b_residual"].abs() > 2.0
)
sensor_df["pressure_sensor_fault"] = (
    sensor_df["pressure_b_residual"].abs() > 1.0
)

print(
    sensor_df[
        ["temp_sensor_fault", "pressure_sensor_fault"]
    ].sum()
)

sensor_df.loc[
    sensor_df["temp_sensor_fault"]
    | sensor_df["pressure_sensor_fault"]
].to_csv(
    OUTPUT_DIR / "ex314_sensor_fault_rows.csv",
    index=False,
    encoding="utf-8-sig",
)
