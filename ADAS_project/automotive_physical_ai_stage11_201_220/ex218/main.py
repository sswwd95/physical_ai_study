import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.anomaly_utils import load_data, output_path
df = load_data()
df["anomaly"] = (
    (df["accel_mps2"].abs() > 1.8) |
    (df["steering_deg"].abs() > 15) |
    (df["ttc_s"] < 2) |
    (df["motor_current_a"] > 7)
)
fig, ax = plt.subplots(figsize=(11,4))
ax.plot(df["time_s"],df["speed_mps"],label="speed")
ax.scatter(df.loc[df["anomaly"],"time_s"],df.loc[df["anomaly"],"speed_mps"],s=12,label="anomaly")
ax.set_xlabel("Time (s)"); ax.set_ylabel("Speed (m/s)"); ax.grid(True); ax.legend()
path = output_path("ex218_anomaly_timeline.png")
fig.tight_layout(); fig.savefig(path,dpi=140); plt.close(fig)
print("saved:", path)
