from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

import numpy as np

sensor_df = pd.read_csv(DATA_FILE)
working_df = sensor_df.copy()

missing_rows = [10, 55, 120, 180, 250]
working_df.loc[missing_rows, "chamber_pressure_pa"] = np.nan

print("보정 전 결측 개수:")
print(working_df.isna().sum())

pressure_median = working_df["chamber_pressure_pa"].median()
working_df["chamber_pressure_pa"] = working_df[
    "chamber_pressure_pa"
].fillna(pressure_median)

print("\n보정 후 결측 개수:")
print(working_df.isna().sum())
working_df.to_csv(
    OUTPUT_DIR / "ex009_filled_missing.csv",
    index=False,
    encoding="utf-8-sig",
)
