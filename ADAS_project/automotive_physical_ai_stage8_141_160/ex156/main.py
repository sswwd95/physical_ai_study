from common.sensor_utils import load_data, output_path
df = load_data()
df["window_10s"] = (df["time_s"] // 10).astype(int)
report = df.groupby("window_10s").agg(
    accel_error_mean=("imu_ax_mps2", "mean"),
    accel_error_std=("imu_ax_mps2", "std"),
    gyro_mean=("imu_gyroz_rps", "mean"),
    gyro_std=("imu_gyroz_rps", "std"),
    encoder_speed_std=("encoder_speed_mps", "std"),
)
path = output_path("ex156_window_noise_statistics.csv")
report.to_csv(path,encoding="utf-8-sig")
print(report.head())
print("saved:", path)
