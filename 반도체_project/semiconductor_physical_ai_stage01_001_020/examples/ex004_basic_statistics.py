from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

sensor_columns = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
]
summary = sensor_df[sensor_columns].describe().loc[
    ["count", "mean", "std", "min", "max"]
]

print(summary.round(3))
summary.to_csv(OUTPUT_DIR / "ex004_basic_statistics.csv", encoding="utf-8-sig")
