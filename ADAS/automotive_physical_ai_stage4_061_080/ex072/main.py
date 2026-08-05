from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
risk = df[(df["front_distance_m"] < 10) & (df["speed_mps"] > 5)].copy()
risk["time_to_collision_s"] = risk["front_distance_m"] / risk["speed_mps"].clip(lower=0.1)
cols = ["timestamp", "time_s", "speed_mps", "front_distance_m", "time_to_collision_s"]
path = output_path("ex072_close_approach.csv")
risk[cols].to_csv(path, index=False, encoding="utf-8-sig")
print(f"risk samples: {len(risk)}")
print(risk[cols].head())
print(f"saved: {path}")
