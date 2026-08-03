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

temp_mean = sensor_df["chamber_temp_c"].mean()
temp_std = sensor_df["chamber_temp_c"].std(ddof=1)
pressure_mean = sensor_df["chamber_pressure_pa"].mean()
pressure_std = sensor_df["chamber_pressure_pa"].std(ddof=1)

sensor_df["temp_ewma"] = (
    sensor_df["chamber_temp_c"]
    .ewm(span=20, adjust=False)
    .mean()
)
sensor_df["temp_ucl"] = temp_mean + 3 * temp_std
sensor_df["temp_lcl"] = temp_mean - 3 * temp_std
sensor_df["pressure_ucl"] = pressure_mean + 3 * pressure_std
sensor_df["pressure_lcl"] = pressure_mean - 3 * pressure_std

sensor_df["spec_violation"] = (
    ~sensor_df["chamber_temp_c"].between(69, 75)
    | ~sensor_df["chamber_pressure_pa"].between(17, 19)
)

sensor_df["risk_score"] = (
    (
        sensor_df["chamber_temp_c"] > sensor_df["temp_ucl"]
    ).astype(int) * 40
    + (
        sensor_df["chamber_pressure_pa"] > sensor_df["pressure_ucl"]
    ).astype(int) * 30
    + (
        sensor_df["vibration_g"] >= 0.15
    ).astype(int) * 20
    + (
        sensor_df["particle_count"] >= 10
    ).astype(int) * 10
)

dashboard_columns = [
    "timestamp",
    "lot_id",
    "chamber_temp_c",
    "chamber_pressure_pa",
    "temp_ewma",
    "temp_ucl",
    "temp_lcl",
    "pressure_ucl",
    "pressure_lcl",
    "spec_violation",
    "risk_score",
]
dashboard_df = sensor_df[dashboard_columns]

print(dashboard_df.tail(10).round(3))
dashboard_df.to_csv(
    OUTPUT_DIR / "ex059_spc_dashboard_data.csv",
    index=False,
    encoding="utf-8-sig",
)
