from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

center_line = sensor_df["chamber_temp_c"].mean()
sensor_df["side"] = np.where(
    sensor_df["chamber_temp_c"] >= center_line,
    1,
    -1,
)

window_size = 7
rolling_sum = (
    sensor_df["side"]
    .rolling(window=window_size)
    .sum()
)

sensor_df["run_rule_violation"] = (
    rolling_sum.abs() == window_size
)

violation_df = sensor_df.loc[
    sensor_df["run_rule_violation"],
    ["timestamp", "chamber_temp_c", "side"],
]

print("런 규칙 위반 행 수:", len(violation_df))
violation_df.to_csv(
    OUTPUT_DIR / "ex050_run_rule_violations.csv",
    index=False,
    encoding="utf-8-sig",
)
