from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE)

lsl = 69.0
usl = 75.0

lot_stats = (
    sensor_df.groupby("lot_id")["chamber_temp_c"]
    .agg(["mean", "std"])
    .reset_index()
)

lot_stats["cp"] = (
    (usl - lsl) / (6 * lot_stats["std"])
)
lot_stats["cpu"] = (
    (usl - lot_stats["mean"]) / (3 * lot_stats["std"])
)
lot_stats["cpl"] = (
    (lot_stats["mean"] - lsl) / (3 * lot_stats["std"])
)
lot_stats["cpk"] = lot_stats[["cpu", "cpl"]].min(axis=1)

lot_stats = lot_stats.sort_values("cpk")

print(lot_stats.round(4))
lot_stats.to_csv(
    OUTPUT_DIR / "ex055_lot_capability.csv",
    index=False,
    encoding="utf-8-sig",
)
