import numpy as np
from common.sensor_utils import load_data, output_path
df = load_data()
dt = df["time_s"].diff().fillna(0)
df["encoder_distance_m"] = np.cumsum(df["encoder_speed_mps"] * dt)
df["true_distance_m"] = np.cumsum(df["true_speed_mps"] * dt)
df["distance_error_m"] = df["encoder_distance_m"] - df["true_distance_m"]
path = output_path("ex154_encoder_distance.csv")
df[["time_s","true_distance_m","encoder_distance_m","distance_error_m"]].to_csv(path,index=False,encoding="utf-8-sig")
print("final distance error:", round(df["distance_error_m"].iloc[-1],4))
print("saved:", path)
