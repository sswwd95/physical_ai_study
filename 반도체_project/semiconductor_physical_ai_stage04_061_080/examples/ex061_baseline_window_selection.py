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

baseline_df = sensor_df.iloc[:120].copy()

rows = []
for column in ["chamber_temp_c", "chamber_pressure_pa"]:
    rows.append({
        "sensor": column,
        "baseline_mean": baseline_df[column].mean(),
        "baseline_std": baseline_df[column].std(ddof=1),
        "overall_mean": sensor_df[column].mean(),
        "overall_std": sensor_df[column].std(ddof=1),
    })

summary_df = pd.DataFrame(rows)
print(summary_df.round(4))
summary_df.to_csv(
    OUTPUT_DIR / "ex061_baseline_summary.csv",
    index=False,
    encoding="utf-8-sig",
)
