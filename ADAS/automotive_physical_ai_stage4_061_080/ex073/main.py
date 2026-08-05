import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
df["ttc_s"] = df["front_distance_m"] / df["speed_mps"].clip(lower=0.5)
df["ttc_s"] = df["ttc_s"].clip(upper=20)
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["time_s"], df["ttc_s"])
ax.axhline(2.0, linestyle="--", label="warning threshold")
ax.set_title("Time To Collision")
ax.set_xlabel("Time (s)")
ax.set_ylabel("TTC (s)")
ax.legend()
ax.grid(True)
fig.tight_layout()
path = output_path("ex073_ttc_timeseries.png")
fig.savefig(path, dpi=140)
plt.close(fig)
print(f"minimum TTC: {df['ttc_s'].min():.2f} s")
print(f"saved: {path}")
