from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

sensor_df["temp_ma10"] = (
    sensor_df["chamber_temp_c"]
    .rolling(window=10, min_periods=1)
    .mean()
)

result_df = sensor_df[["timestamp", "chamber_temp_c", "temp_ma10"]]
print(result_df.tail(20).round(3))
result_df.to_csv(
    OUTPUT_DIR / "ex013_temperature_moving_average.csv",
    index=False,
    encoding="utf-8-sig",
)
