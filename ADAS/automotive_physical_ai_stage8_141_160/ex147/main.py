import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.sensor_utils import load_data, output_path
df = load_data()
error = df["imu_ax_mps2"] - df["true_accel_mps2"]
fig, ax = plt.subplots(figsize=(8,4))
ax.hist(error, bins=60)
ax.set_title("Accelerometer Error Distribution")
ax.set_xlabel("Error (m/s^2)")
ax.set_ylabel("Frequency")
ax.grid(True)
path = output_path("ex147_accel_error_histogram.png")
fig.tight_layout(); fig.savefig(path,dpi=140); plt.close(fig)
print("saved:", path)
