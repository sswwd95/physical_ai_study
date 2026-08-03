from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

top_particle_df = (
    sensor_df[
        ["timestamp", "lot_id", "particle_count", "chamber_temp_c"]
    ]
    .sort_values("particle_count", ascending=False)
    .head(15)
)

print(top_particle_df)
top_particle_df.to_csv(
    OUTPUT_DIR / "ex011_top_particle_count.csv",
    index=False,
    encoding="utf-8-sig",
)
