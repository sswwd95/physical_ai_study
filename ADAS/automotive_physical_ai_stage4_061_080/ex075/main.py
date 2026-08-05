import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
x = df["steering_deg"].to_numpy()
y = df["yaw_rate_rps"].to_numpy()
slope, intercept = np.polyfit(x, y, 1)
line_x = np.linspace(x.min(), x.max(), 100)
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(x, y, s=9, alpha=0.4)
ax.plot(line_x, slope * line_x + intercept)
ax.set_title("Steering Angle vs Yaw Rate")
ax.set_xlabel("Steering (deg)")
ax.set_ylabel("Yaw Rate (rad/s)")
ax.grid(True)
fig.tight_layout()
path = output_path("ex075_steering_yaw_relation.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(f"linear fit: yaw_rate = {slope:.4f} * steering + {intercept:.4f}")
print(f"saved: {path}")
