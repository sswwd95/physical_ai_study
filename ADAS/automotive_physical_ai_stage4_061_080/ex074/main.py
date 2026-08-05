import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
df["wheel_speed_diff"] = df["wheel_right_mps"] - df["wheel_left_mps"]
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["time_s"], df["wheel_speed_diff"])
ax.set_title("Left-Right Wheel Speed Difference")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Difference (m/s)")
ax.grid(True)
fig.tight_layout()
path = output_path("ex074_wheel_speed_difference.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(df["wheel_speed_diff"].describe())
print(f"saved: {path}")
