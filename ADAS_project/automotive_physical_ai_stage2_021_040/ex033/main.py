from common.load_data import load_vehicle_log

df = load_vehicle_log()
df["speed_kph"] = df["speed_mps"] * 3.6
df["steering_direction"] = "STRAIGHT"
df.loc[df["steering_deg"] > 1.0, "steering_direction"] = "LEFT"
df.loc[df["steering_deg"] < -1.0, "steering_direction"] = "RIGHT"
print(df[["speed_mps", "speed_kph", "steering_deg", "steering_direction"]].head(12))
