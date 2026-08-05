import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["time_s"], df["speed_mps"])
ax.set_title("Vehicle Speed Time Series")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Speed (m/s)")
ax.grid(True)
fig.tight_layout()
path = output_path("ex061_speed_timeseries.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(f"saved: {path}")
