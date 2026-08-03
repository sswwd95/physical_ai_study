from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

lot_summary = (
    sensor_df.groupby("lot_id")
    .agg(
        temp_mean=("chamber_temp_c", "mean"),
        temp_std=("chamber_temp_c", "std"),
        pressure_mean=("chamber_pressure_pa", "mean"),
        pressure_std=("chamber_pressure_pa", "std"),
        particle_mean=("particle_count", "mean"),
    )
    .reset_index()
)

print(lot_summary.round(3))
lot_summary.to_csv(
    OUTPUT_DIR / "ex007_lot_summary.csv",
    index=False,
    encoding="utf-8-sig",
)
