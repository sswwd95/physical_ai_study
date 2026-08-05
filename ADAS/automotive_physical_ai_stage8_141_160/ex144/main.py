from common.sensor_utils import load_data
df = load_data()
stationary = df[df["time_s"] < 5.0]
accel_bias = (stationary["imu_ax_mps2"] - stationary["true_accel_mps2"]).mean()
gyro_bias = (stationary["imu_gyroz_rps"] - stationary["true_yaw_rate_rps"]).mean()
print("estimated accel bias:", round(accel_bias, 6))
print("estimated gyro bias:", round(gyro_bias, 6))
