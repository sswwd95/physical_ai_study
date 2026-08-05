from common.sensor_utils import load_data, rmse
df = load_data()
error = df["imu_ax_mps2"] - df["true_accel_mps2"]
print("mean error:", round(error.mean(), 6))
print("std error:", round(error.std(), 6))
print("RMSE:", round(rmse(df["imu_ax_mps2"], df["true_accel_mps2"]), 6))
