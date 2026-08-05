import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
conditions = [
    df["speed_mps"] < 0.5,
    df["accel_mps2"] >= 1.0,
    df["accel_mps2"] <= -1.0,
    df["steering_deg"].abs() >= 8,
]
codes = np.select(conditions, [0, 2, 3, 4], default=1)
fig, ax = plt.subplots(figsize=(10, 3))
ax.step(df["time_s"], codes, where="post")
ax.set_yticks([0, 1, 2, 3, 4], ["STOP", "CRUISE", "ACCEL", "DECEL", "TURN"])
ax.set_title("Driving State Timeline")
ax.set_xlabel("Time (s)")
ax.grid(True)
fig.tight_layout()
path = output_path("ex078_driving_state_timeline.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(f"saved: {path}")
