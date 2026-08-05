from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
cols = ["speed_mps", "accel_mps2", "steering_deg", "yaw_rate_rps",
        "front_distance_m", "motor_current_a", "battery_voltage_v"]
corr = df[cols].corr()
path = output_path("ex065_correlation_matrix.csv")
corr.to_csv(path, encoding="utf-8-sig")
print(corr.round(3))
print(f"saved: {path}")
