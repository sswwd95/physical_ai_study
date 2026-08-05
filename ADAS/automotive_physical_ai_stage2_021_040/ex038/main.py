from common.load_data import load_vehicle_log

df = load_vehicle_log()
dt = df["time_s"].diff()
df["estimated_accel"] = df["speed_mps"].diff() / dt
candidates = df.loc[df["estimated_accel"].abs() > 2.5, ["time_s", "speed_mps", "estimated_accel"]]
print(candidates.head(20).round(3))
print("급변 후보 수:", len(candidates))
