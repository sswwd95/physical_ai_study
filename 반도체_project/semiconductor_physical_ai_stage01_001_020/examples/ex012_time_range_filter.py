from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

start_time = pd.Timestamp("2026-01-01 09:02:00")
end_time = pd.Timestamp("2026-01-01 09:02:30")

time_mask = sensor_df["timestamp"].between(start_time, end_time)
time_slice_df = sensor_df.loc[
    time_mask,
    ["timestamp", "chamber_temp_c", "chamber_pressure_pa", "vibration_g"],
]

print(time_slice_df)
