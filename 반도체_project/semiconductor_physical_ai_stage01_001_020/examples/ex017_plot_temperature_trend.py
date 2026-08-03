from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

plt.figure(figsize=(12, 5))
plt.plot(
    sensor_df["timestamp"],
    sensor_df["chamber_temp_c"],
    label="Chamber temperature",
)
plt.axhline(75.0, linestyle="--", label="75 C threshold")
plt.title("Semiconductor Chamber Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "ex017_temperature_trend.png", dpi=150)
plt.close()

print("그래프 저장 완료")
