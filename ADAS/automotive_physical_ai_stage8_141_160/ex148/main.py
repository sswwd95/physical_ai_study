import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.sensor_utils import load_data, output_path
df = load_data()
error = df["imu_gyroz_rps"] - df["true_yaw_rate_rps"]
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(df["time_s"], error)
ax.set_title("Gyroscope Error and Drift")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Error (rad/s)")
ax.grid(True)
path = output_path("ex148_gyro_drift.png")
fig.tight_layout(); fig.savefig(path,dpi=140); plt.close(fig)
print("saved:", path)
