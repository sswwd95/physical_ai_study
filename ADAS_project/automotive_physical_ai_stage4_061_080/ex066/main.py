import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
cols = ["speed_mps", "accel_mps2", "steering_deg", "yaw_rate_rps",
        "front_distance_m", "motor_current_a", "battery_voltage_v"]
corr = df[cols].corr()
fig, ax = plt.subplots(figsize=(8, 6))
image = ax.imshow(corr, vmin=-1, vmax=1)
ax.set_xticks(range(len(cols)), cols, rotation=45, ha="right")
ax.set_yticks(range(len(cols)), cols)
fig.colorbar(image, ax=ax, label="Correlation")
ax.set_title("Sensor Correlation Heatmap")
fig.tight_layout()
path = output_path("ex066_correlation_heatmap.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(f"saved: {path}")
