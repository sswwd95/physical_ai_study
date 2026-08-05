from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

baseline = sensor_df["chamber_temp_c"].iloc[:120]
mean_value = baseline.mean()
std_value = baseline.std(ddof=1)

sensor_df["temp_standardized_residual"] = (
    sensor_df["chamber_temp_c"] - mean_value
) / std_value

count_2 = int(
    (sensor_df["temp_standardized_residual"].abs() >= 2).sum()
)
count_3 = int(
    (sensor_df["temp_standardized_residual"].abs() >= 3).sum()
)

print("절댓값 2 이상:", count_2)
print("절댓값 3 이상:", count_3)

sensor_df.to_csv(
    OUTPUT_DIR / "ex062_standardized_residuals.csv",
    index=False,
    encoding="utf-8-sig",
)
