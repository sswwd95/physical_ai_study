import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
df["ttc_s"] = (df["front_distance_m"] / df["speed_mps"].clip(lower=0.5)).clip(upper=20)
df["risk_flag"] = (df["ttc_s"] < 2.0) & (df["speed_mps"] > 3.0)
df["state"] = np.select(
    [
        df["speed_mps"] < 0.5,
        df["accel_mps2"] >= 1.0,
        df["accel_mps2"] <= -1.0,
        df["steering_deg"].abs() >= 8,
    ],
    ["STOP", "ACCELERATE", "DECELERATE", "TURN"],
    default="CRUISE",
)

fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
axes[0].plot(df["time_s"], df["speed_mps"])
axes[0].set_ylabel("Speed")
axes[0].grid(True)
axes[1].plot(df["time_s"], df["accel_mps2"])
axes[1].set_ylabel("Accel")
axes[1].grid(True)
axes[2].plot(df["time_s"], df["steering_deg"])
axes[2].set_ylabel("Steering")
axes[2].grid(True)
axes[3].plot(df["time_s"], df["ttc_s"])
axes[3].axhline(2.0, linestyle="--")
axes[3].set_ylabel("TTC")
axes[3].set_xlabel("Time (s)")
axes[3].grid(True)
fig.suptitle("Integrated Driving Analysis Dashboard")
fig.tight_layout()
dashboard_path = output_path("ex080_integrated_dashboard.png")
fig.savefig(dashboard_path, dpi=140)
plt.close(fig)

summary = {
    "samples": int(len(df)),
    "duration_s": float(df["time_s"].max()),
    "mean_speed_mps": float(df["speed_mps"].mean()),
    "max_speed_mps": float(df["speed_mps"].max()),
    "minimum_ttc_s": float(df["ttc_s"].min()),
    "risk_samples": int(df["risk_flag"].sum()),
    "state_counts": df["state"].value_counts().to_dict(),
}
summary_path = output_path("ex080_summary.json")
summary_path.write_text(
    __import__("json").dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(summary)
print(f"saved: {dashboard_path}")
print(f"saved: {summary_path}")
