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

sensor_columns = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "vibration_g",
]

score = np.zeros(len(sensor_df))

for column in sensor_columns:
    baseline = sensor_df[column].iloc[:120]
    z = (
        sensor_df[column] - baseline.mean()
    ) / baseline.std(ddof=1)
    sensor_df[f"{column}_z"] = z
    score += z.abs()

sensor_df["change_score"] = score
sensor_df["change_alarm"] = (
    sensor_df["change_score"] >= 8.0
)

top_df = (
    sensor_df.sort_values(
        "change_score",
        ascending=False,
    )
    .head(20)
)

print(top_df[
    ["timestamp", "lot_id", "change_score", "change_alarm"]
].round(3))
top_df.to_csv(
    OUTPUT_DIR / "ex073_multi_sensor_change_score.csv",
    index=False,
    encoding="utf-8-sig",
)
