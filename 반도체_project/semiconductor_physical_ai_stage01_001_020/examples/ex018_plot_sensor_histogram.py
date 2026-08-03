from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sensor_df = pd.read_csv(DATA_FILE)
pressure_mean = sensor_df["chamber_pressure_pa"].mean()

plt.figure(figsize=(8, 5))
plt.hist(sensor_df["chamber_pressure_pa"], bins=25, alpha=0.8)
plt.axvline(pressure_mean, linestyle="--", label=f"Mean={pressure_mean:.2f}")
plt.title("Chamber Pressure Distribution")
plt.xlabel("Pressure (Pa)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "ex018_pressure_histogram.png", dpi=150)
plt.close()

print(f"압력 평균: {pressure_mean:.3f} Pa")
