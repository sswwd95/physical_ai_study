from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/digital_twin_sensor_stream.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])
sensor_df = sensor_df.sort_values("timestamp")

interval = sensor_df["timestamp"].diff().dt.total_seconds()
result_df = pd.DataFrame({
    "timestamp": sensor_df["timestamp"],
    "interval_seconds": interval,
})
result_df["interval_error"] = result_df["interval_seconds"].ne(1.0)

print("기대 간격과 다른 행:", int(result_df["interval_error"].sum()))
print(result_df["interval_seconds"].describe())
result_df.to_csv(
    OUTPUT_DIR / "ex302_timestamp_validation.csv",
    index=False,
    encoding="utf-8-sig",
)
