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

mean_value = sensor_df["chamber_pressure_pa"].mean()
std_value = sensor_df["chamber_pressure_pa"].std(ddof=1)

upper_2s = mean_value + 2 * std_value
lower_2s = mean_value - 2 * std_value

above_upper = (
    sensor_df["chamber_pressure_pa"] > upper_2s
).astype(int)
below_lower = (
    sensor_df["chamber_pressure_pa"] < lower_2s
).astype(int)

upper_count = above_upper.rolling(window=3).sum()
lower_count = below_lower.rolling(window=3).sum()

sensor_df["zone_rule_violation"] = (
    (upper_count >= 2)
    | (lower_count >= 2)
)

violation_df = sensor_df.loc[
    sensor_df["zone_rule_violation"],
    ["timestamp", "chamber_pressure_pa"],
]

print("Zone 규칙 위반 행 수:", len(violation_df))
violation_df.to_csv(
    OUTPUT_DIR / "ex052_zone_rule_violations.csv",
    index=False,
    encoding="utf-8-sig",
)
