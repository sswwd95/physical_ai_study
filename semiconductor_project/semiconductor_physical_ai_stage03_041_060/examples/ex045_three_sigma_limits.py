from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

pressure_mean = sensor_df["chamber_pressure_pa"].mean()
pressure_std = sensor_df["chamber_pressure_pa"].std(ddof=1)

cl = pressure_mean
ucl = pressure_mean + 3 * pressure_std
lcl = pressure_mean - 3 * pressure_std

sensor_df["pressure_out_of_control"] = (
    (sensor_df["chamber_pressure_pa"] > ucl)
    | (sensor_df["chamber_pressure_pa"] < lcl)
)

problem_df = sensor_df.loc[
    sensor_df["pressure_out_of_control"],
    ["timestamp", "lot_id", "chamber_pressure_pa"],
]

print(f"CL={cl:.3f}, UCL={ucl:.3f}, LCL={lcl:.3f}")
print("관리한계 이탈 수:", len(problem_df))
print(problem_df.round(3))

problem_df.to_csv(
    OUTPUT_DIR / "ex045_pressure_out_of_control.csv",
    index=False,
    encoding="utf-8-sig",
)
