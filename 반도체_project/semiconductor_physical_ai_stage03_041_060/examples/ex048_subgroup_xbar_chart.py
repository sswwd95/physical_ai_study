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

subgroup_df = (
    sensor_df.groupby("subgroup_id")
    .agg(
        subgroup_mean=("chamber_temp_c", "mean"),
        subgroup_min=("chamber_temp_c", "min"),
        subgroup_max=("chamber_temp_c", "max"),
    )
    .reset_index()
)
subgroup_df["subgroup_range"] = (
    subgroup_df["subgroup_max"]
    - subgroup_df["subgroup_min"]
)

x_double_bar = subgroup_df["subgroup_mean"].mean()
r_bar = subgroup_df["subgroup_range"].mean()
a2 = 0.577

subgroup_df["cl"] = x_double_bar
subgroup_df["ucl"] = x_double_bar + a2 * r_bar
subgroup_df["lcl"] = x_double_bar - a2 * r_bar
subgroup_df["out_of_control"] = (
    (subgroup_df["subgroup_mean"] > subgroup_df["ucl"])
    | (subgroup_df["subgroup_mean"] < subgroup_df["lcl"])
)

print(subgroup_df.head(10).round(3))
print(
    "X-bar 이탈 소그룹:",
    int(subgroup_df["out_of_control"].sum()),
)

subgroup_df.to_csv(
    OUTPUT_DIR / "ex048_xbar_chart_data.csv",
    index=False,
    encoding="utf-8-sig",
)
