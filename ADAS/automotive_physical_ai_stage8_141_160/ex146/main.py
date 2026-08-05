from common.sensor_utils import load_data, moving_average, rmse, output_path
df = load_data()
df["imu_ax_ma"] = moving_average(df["imu_ax_mps2"], 21)
print("raw RMSE:", round(rmse(df["imu_ax_mps2"], df["true_accel_mps2"]), 6))
print("smoothed RMSE:", round(rmse(df["imu_ax_ma"], df["true_accel_mps2"]), 6))
path = output_path("ex146_accel_moving_average.csv")
df[["time_s","true_accel_mps2","imu_ax_mps2","imu_ax_ma"]].to_csv(path,index=False,encoding="utf-8-sig")
print("saved:", path)
