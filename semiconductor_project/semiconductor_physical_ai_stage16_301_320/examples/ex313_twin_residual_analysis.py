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

sensor_df["temp_residual"] = (
    sensor_df["temp_sensor_a_c"]
    - sensor_df["true_temperature_c"]
)
sensor_df["pressure_residual"] = (
    sensor_df["pressure_sensor_a_pa"]
    - sensor_df["true_pressure_pa"]
)

summary_df = sensor_df.groupby("process_phase")[
    ["temp_residual", "pressure_residual"]
].agg(["mean", "std", "max", "min"])

print(summary_df.round(4))
summary_df.to_csv(
    OUTPUT_DIR / "ex313_twin_residual_summary.csv",
    encoding="utf-8-sig",
)
