import numpy as np
from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
conditions = [
    df["speed_mps"] < 0.5,
    df["accel_mps2"] >= 1.0,
    df["accel_mps2"] <= -1.0,
    df["steering_deg"].abs() >= 8,
]
labels = ["STOP", "ACCELERATE", "DECELERATE", "TURN"]
df["driving_state"] = np.select(conditions, labels, default="CRUISE")
summary = df["driving_state"].value_counts().rename_axis("state").reset_index(name="samples")
summary["ratio_pct"] = summary["samples"] / len(df) * 100
path = output_path("ex077_driving_state_summary.csv")
summary.to_csv(path, index=False, encoding="utf-8-sig")
print(summary)
print(f"saved: {path}")
