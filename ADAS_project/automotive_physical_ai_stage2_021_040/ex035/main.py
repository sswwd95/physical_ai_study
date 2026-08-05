from common.load_data import load_vehicle_log

df = load_vehicle_log()
result = df.nsmallest(10, "front_distance_m")
print(result[["time_s", "speed_mps", "front_distance_m", "status"]])
