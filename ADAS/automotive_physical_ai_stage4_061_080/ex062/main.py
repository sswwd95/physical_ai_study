import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["time_s"], df["speed_mps"], label="speed")
ax.plot(df["time_s"], df["front_distance_m"], label="front distance")
ax.set_title("Speed and Front Distance")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Value")
ax.legend()
ax.grid(True)
fig.tight_layout()
path = output_path("ex062_multi_sensor.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(f"saved: {path}")
