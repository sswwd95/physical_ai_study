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

sensor_columns = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
]

lot_mean = sensor_df.groupby("lot_id")[sensor_columns].mean()
overall_mean = sensor_df[sensor_columns].mean()

difference = lot_mean.subtract(overall_mean, axis="columns")
difference.columns = [f"{column}_diff" for column in difference.columns]

result_df = pd.concat([lot_mean, difference], axis=1)

print(result_df.round(3))
result_df.to_csv(
    OUTPUT_DIR / "ex042_lot_mean_comparison.csv",
    encoding="utf-8-sig",
)
