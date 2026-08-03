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

for lambda_value in [0.05, 0.2, 0.5]:
    column = f"temp_ewma_{str(lambda_value).replace('.', '_')}"
    sensor_df[column] = (
        sensor_df["chamber_temp_c"]
        .ewm(alpha=lambda_value, adjust=False)
        .mean()
    )

result_columns = [
    "timestamp",
    "chamber_temp_c",
    "temp_ewma_0_05",
    "temp_ewma_0_2",
    "temp_ewma_0_5",
]
result_df = sensor_df[result_columns]

print(result_df.tail(20).round(4))
result_df.to_csv(
    OUTPUT_DIR / "ex068_ewma_lambda_comparison.csv",
    index=False,
    encoding="utf-8-sig",
)
