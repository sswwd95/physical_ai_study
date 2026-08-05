from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

selected_columns = [
    "timestamp",
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
]
selected_df = sensor_df[selected_columns]

print(selected_df.head(10))
selected_df.to_csv(
    OUTPUT_DIR / "ex003_selected_columns.csv",
    index=False,
    encoding="utf-8-sig",
)
