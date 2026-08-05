import numpy as np
from common.sensor_utils import load_data, rmse, output_path
df = load_data()
dt = df["time_s"].diff().fillna(0).to_numpy()
df["yaw_from_gyro"] = np.cumsum(df["imu_gyroz_rps"].to_numpy() * dt)
df["yaw_error_rad"] = df["yaw_from_gyro"] - df["true_yaw_rad"]
print("final yaw error:", round(df["yaw_error_rad"].iloc[-1], 6))
print("yaw RMSE:", round(rmse(df["yaw_from_gyro"], df["true_yaw_rad"]), 6))
path = output_path("ex149_gyro_integrated_yaw.csv")
df[["time_s","true_yaw_rad","yaw_from_gyro","yaw_error_rad"]].to_csv(path,index=False,encoding="utf-8-sig")
print("saved:", path)
