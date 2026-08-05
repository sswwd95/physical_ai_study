import numpy as np
from common.anomaly_utils import load_data, output_path
df = load_data()
conditions = [
    df["speed_mps"] < 0.5,
    df["accel_mps2"] > 1.2,
    df["accel_mps2"] < -1.2,
    df["steering_deg"].abs() > 10,
]
labels = ["STOP","ACCELERATE","DECELERATE","TURN"]
df["driving_state"] = np.select(conditions, labels, default="CRUISE")
summary = df["driving_state"].value_counts().rename_axis("state").reset_index(name="samples")
path = output_path("ex202_driving_state_summary.csv")
summary.to_csv(path,index=False,encoding="utf-8-sig")
print(summary)
print("saved:", path)
