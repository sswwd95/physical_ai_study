from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

high_temp_mask = sensor_df["chamber_temp_c"] >= 75.0
high_temp_df = sensor_df.loc[
    high_temp_mask,
    ["timestamp", "lot_id", "chamber_temp_c", "chamber_pressure_pa"],
]

print(f"고온 행 개수: {len(high_temp_df)}")
print(high_temp_df.head(20))
high_temp_df.to_csv(
    OUTPUT_DIR / "ex005_high_temperature.csv",
    index=False,
    encoding="utf-8-sig",
)
