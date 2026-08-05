from common.load_data import load_vehicle_log

df = load_vehicle_log()
df["speed_ma5"] = df["speed_mps"].rolling(window=5, min_periods=1).mean()
print(df[["time_s", "speed_mps", "speed_ma5"]].head(15).round(3))
