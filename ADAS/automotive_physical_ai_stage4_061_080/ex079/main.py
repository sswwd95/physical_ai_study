from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
df["window_10s"] = (df["time_s"] // 10).astype(int)
report = df.groupby("window_10s").agg(
    start_time_s=("time_s", "min"),
    end_time_s=("time_s", "max"),
    mean_speed_mps=("speed_mps", "mean"),
    max_speed_mps=("speed_mps", "max"),
    min_distance_m=("front_distance_m", "min"),
    max_abs_accel=("accel_mps2", lambda s: s.abs().max()),
    max_abs_steering=("steering_deg", lambda s: s.abs().max()),
    mean_current_a=("motor_current_a", "mean"),
)
path = output_path("ex079_window_statistics.csv")
report.to_csv(path, encoding="utf-8-sig")
print(report.round(3))
print(f"saved: {path}")
