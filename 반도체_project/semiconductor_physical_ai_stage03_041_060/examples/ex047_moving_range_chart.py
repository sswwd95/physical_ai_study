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

sensor_df["moving_range"] = (
    sensor_df["chamber_temp_c"]
    .diff()
    .abs()
)

mr_mean = sensor_df["moving_range"].mean()
mr_ucl = 3.267 * mr_mean

sensor_df["mr_out_of_control"] = (
    sensor_df["moving_range"] > mr_ucl
)

plt.figure(figsize=(12, 5))
plt.plot(
    sensor_df["timestamp"],
    sensor_df["moving_range"],
    label="Moving range",
)
plt.axhline(mr_mean, linestyle="-", label="MR mean")
plt.axhline(mr_ucl, linestyle="--", label="MR UCL")
plt.title("Temperature Moving Range Chart")
plt.xlabel("Time")
plt.ylabel("Moving range")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "ex047_temperature_mr_chart.png",
    dpi=150,
)
plt.close()

print(f"MR 평균={mr_mean:.3f}, UCL={mr_ucl:.3f}")
print(
    "MR 관리한계 이탈 수:",
    int(sensor_df["mr_out_of_control"].sum()),
)
