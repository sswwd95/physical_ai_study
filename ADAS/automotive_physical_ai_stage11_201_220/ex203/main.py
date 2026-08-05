from common.anomaly_utils import load_data, output_path
df = load_data()
events = df[df["accel_mps2"] > 1.8].copy()
path = output_path("ex203_hard_acceleration.csv")
events.to_csv(path,index=False,encoding="utf-8-sig")
print("detected samples:", len(events))
print(events[["time_s","accel_mps2","event_label"]].head())
