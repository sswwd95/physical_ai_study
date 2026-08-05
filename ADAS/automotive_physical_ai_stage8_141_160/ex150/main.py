import numpy as np
from common.sensor_utils import load_data, rmse, output_path
df = load_data()
bias = (df.loc[df["time_s"] < 5, "imu_gyroz_rps"] - df.loc[df["time_s"] < 5, "true_yaw_rate_rps"]).mean()
dt = df["time_s"].diff().fillna(0).to_numpy()
df["gyro_corrected"] = df["imu_gyroz_rps"] - bias
df["yaw_corrected"] = np.cumsum(df["gyro_corrected"].to_numpy() * dt)
print("estimated bias:", round(bias,6))
print("corrected yaw RMSE:", round(rmse(df["yaw_corrected"], df["true_yaw_rad"]), 6))
path = output_path("ex150_corrected_yaw.csv")
df[["time_s","true_yaw_rad","yaw_corrected"]].to_csv(path,index=False,encoding="utf-8-sig")
print("saved:", path)
