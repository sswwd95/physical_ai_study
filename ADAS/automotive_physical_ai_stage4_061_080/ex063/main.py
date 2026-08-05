import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(df["accel_mps2"], bins=40)
ax.set_title("Acceleration Distribution")
ax.set_xlabel("Acceleration (m/s^2)")
ax.set_ylabel("Frequency")
ax.grid(True)
fig.tight_layout()
path = output_path("ex063_acceleration_histogram.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(df["accel_mps2"].describe())
print(f"saved: {path}")
