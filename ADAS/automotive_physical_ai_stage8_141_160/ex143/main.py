from common.sensor_utils import load_data, rmse
df = load_data()
error = df["imu_gyroz_rps"] - df["true_yaw_rate_rps"]
print("mean error:", round(error.mean(), 6))
print("std error:", round(error.std(), 6))
print("RMSE:", round(rmse(df["imu_gyroz_rps"], df["true_yaw_rate_rps"]), 6))
