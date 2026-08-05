from common.anomaly_utils import load_data, output_path
df = load_data()
events = df[(df["front_distance_m"] < 7) & (df["speed_mps"] > 3)].copy()
path = output_path("ex206_close_approach.csv")
events.to_csv(path,index=False,encoding="utf-8-sig")
print("detected samples:", len(events))
print(events[["time_s","front_distance_m","ttc_s","event_label"]].head())
