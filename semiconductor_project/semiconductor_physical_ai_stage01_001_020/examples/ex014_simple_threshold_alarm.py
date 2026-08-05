from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

alarm_mask = (
    (sensor_df["chamber_temp_c"] >= 75.0)
    | (sensor_df["chamber_pressure_pa"] >= 20.0)
    | (sensor_df["vibration_g"] >= 0.15)
)
sensor_df["alarm"] = alarm_mask.astype(int)

alarm_df = sensor_df.loc[
    sensor_df["alarm"] == 1,
    [
        "timestamp",
        "lot_id",
        "chamber_temp_c",
        "chamber_pressure_pa",
        "vibration_g",
        "alarm",
    ],
]

print("경보 건수:", len(alarm_df))
print(alarm_df.head(30).round(3))
