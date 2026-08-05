from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE)

subgroup_size = 5
sensor_df["subgroup_id"] = (
    np.arange(len(sensor_df)) // subgroup_size
)

range_df = (
    sensor_df.groupby("subgroup_id")["chamber_temp_c"]
    .agg(["min", "max"])
    .reset_index()
)
range_df["subgroup_range"] = range_df["max"] - range_df["min"]

r_bar = range_df["subgroup_range"].mean()
d3 = 0.0
d4 = 2.114

range_df["cl"] = r_bar
range_df["ucl"] = d4 * r_bar
range_df["lcl"] = d3 * r_bar
range_df["out_of_control"] = (
    (range_df["subgroup_range"] > range_df["ucl"])
    | (range_df["subgroup_range"] < range_df["lcl"])
)

print(f"Rbar={r_bar:.3f}")
print(
    "R 관리도 이탈 소그룹:",
    int(range_df["out_of_control"].sum()),
)
print(range_df.loc[range_df["out_of_control"]])

range_df.to_csv(
    OUTPUT_DIR / "ex049_r_chart_data.csv",
    index=False,
    encoding="utf-8-sig",
)
