from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

from scipy.stats import zscore

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

sensor_df["temp_zscore"] = zscore(sensor_df["chamber_temp_c"])
outlier_df = sensor_df.loc[
    sensor_df["temp_zscore"].abs() >= 3.0,
    ["timestamp", "lot_id", "chamber_temp_c", "temp_zscore"],
]

print("온도 이상 후보 수:", len(outlier_df))
print(outlier_df.round(3))
