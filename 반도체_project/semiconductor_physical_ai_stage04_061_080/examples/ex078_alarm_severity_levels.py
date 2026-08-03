from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE)

score = np.zeros(len(sensor_df))

for column in [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "vibration_g",
]:
    baseline = sensor_df[column].iloc[:120]
    z = (
        sensor_df[column] - baseline.mean()
    ) / baseline.std(ddof=1)
    score += z.abs()

sensor_df["change_score"] = score
sensor_df["severity"] = pd.cut(
    sensor_df["change_score"],
    bins=[-np.inf, 4, 8, 12, np.inf],
    labels=["normal", "caution", "warning", "critical"],
    right=False,
)

print(sensor_df["severity"].value_counts().sort_index())
sensor_df.to_csv(
    OUTPUT_DIR / "ex078_alarm_severity.csv",
    index=False,
    encoding="utf-8-sig",
)
