from common.load_data import load_vehicle_log

df = load_vehicle_log()
summary = df.groupby("status")[["speed_mps", "front_distance_m", "motor_temp_c"]].agg(["count", "mean", "std"])
print(summary.round(3))
