import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
df["speed_ma_20"] = df["speed_mps"].rolling(20, min_periods=1).mean()
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["time_s"], df["speed_mps"], alpha=0.35, label="raw")
ax.plot(df["time_s"], df["speed_ma_20"], label="moving average")
ax.set_title("Speed Smoothing")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Speed (m/s)")
ax.legend()
ax.grid(True)
fig.tight_layout()
path = output_path("ex067_speed_moving_average.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(f"saved: {path}")
