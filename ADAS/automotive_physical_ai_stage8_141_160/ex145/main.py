from common.sensor_utils import load_data, rmse, output_path
df = load_data()
stationary = df[df["time_s"] < 5.0]
bias = (stationary["imu_ax_mps2"] - stationary["true_accel_mps2"]).mean()
df["imu_ax_corrected"] = df["imu_ax_mps2"] - bias
print("before RMSE:", round(rmse(df["imu_ax_mps2"], df["true_accel_mps2"]), 6))
print("after RMSE:", round(rmse(df["imu_ax_corrected"], df["true_accel_mps2"]), 6))
path = output_path("ex145_bias_corrected_accel.csv")
df[["time_s","true_accel_mps2","imu_ax_mps2","imu_ax_corrected"]].to_csv(path,index=False,encoding="utf-8-sig")
print("saved:", path)
