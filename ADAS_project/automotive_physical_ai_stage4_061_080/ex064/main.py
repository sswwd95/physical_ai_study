import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(df["speed_mps"], df["motor_current_a"], s=10, alpha=0.5)
ax.set_title("Speed vs Motor Current")
ax.set_xlabel("Speed (m/s)")
ax.set_ylabel("Motor Current (A)")
ax.grid(True)
fig.tight_layout()
path = output_path("ex064_speed_current_scatter.png")
fig.savefig(path, dpi=140)
plt.close(fig)
corr = df["speed_mps"].corr(df["motor_current_a"])
print(f"Pearson correlation: {corr:.3f}")
print(f"saved: {path}")
