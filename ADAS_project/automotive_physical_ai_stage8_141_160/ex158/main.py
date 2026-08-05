from common.sensor_utils import load_data, rmse, output_path
df = load_data()
scale = 0.995
offset = 0.045
df["accel_calibrated"] = (df["imu_ax_mps2"] - offset) / scale
print("raw RMSE:", round(rmse(df["imu_ax_mps2"], df["true_accel_mps2"]),6))
print("calibrated RMSE:", round(rmse(df["accel_calibrated"], df["true_accel_mps2"]),6))
path = output_path("ex158_accel_calibrated.csv")
df[["time_s","true_accel_mps2","imu_ax_mps2","accel_calibrated"]].to_csv(path,index=False,encoding="utf-8-sig")
print("saved:", path)
