from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

mean_value = sensor_df["chamber_temp_c"].mean()
std_value = sensor_df["chamber_temp_c"].std(ddof=1)
ucl = mean_value + 3 * std_value
lcl = mean_value - 3 * std_value

outlier_mask = (
    (sensor_df["chamber_temp_c"] > ucl)
    | (sensor_df["chamber_temp_c"] < lcl)
)

plt.figure(figsize=(12, 5))
plt.plot(
    sensor_df["timestamp"],
    sensor_df["chamber_temp_c"],
    label="Temperature",
)
plt.axhline(mean_value, linestyle="-", label="CL")
plt.axhline(ucl, linestyle="--", label="UCL")
plt.axhline(lcl, linestyle="--", label="LCL")
plt.scatter(
    sensor_df.loc[outlier_mask, "timestamp"],
    sensor_df.loc[outlier_mask, "chamber_temp_c"],
    label="Out of control",
)
plt.title("Temperature Individuals Control Chart")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "ex046_temperature_i_chart.png",
    dpi=150,
)
plt.close()

print("I 관리도 저장 완료")
