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

values = sensor_df["chamber_temp_c"].to_numpy()
rows = []

for split_index in range(60, len(values) - 60, 5):
    before_mean = values[:split_index].mean()
    after_mean = values[split_index:].mean()
    rows.append({
        "split_index": split_index,
        "before_mean": before_mean,
        "after_mean": after_mean,
        "absolute_mean_difference": abs(after_mean - before_mean),
    })

scan_df = (
    pd.DataFrame(rows)
    .sort_values(
        "absolute_mean_difference",
        ascending=False,
    )
    .head(10)
)

print(scan_df.round(4))
scan_df.to_csv(
    OUTPUT_DIR / "ex071_mean_shift_candidates.csv",
    index=False,
    encoding="utf-8-sig",
)
