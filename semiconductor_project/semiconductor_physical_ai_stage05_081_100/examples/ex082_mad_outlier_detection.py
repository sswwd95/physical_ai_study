from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

values = sensor_df["chamber_temp_c"]
median_value = values.median()
mad = np.median(np.abs(values - median_value))

sensor_df["temp_modified_z"] = (
    0.6745 * (values - median_value) / mad
)
sensor_df["mad_anomaly"] = (
    sensor_df["temp_modified_z"].abs() >= 3.5
)

print("MAD 이상치 수:", int(sensor_df["mad_anomaly"].sum()))
sensor_df.to_csv(
    OUTPUT_DIR / "ex082_mad_outliers.csv",
    index=False,
    encoding="utf-8-sig",
)
