from common.anomaly_utils import load_data, output_path
df = load_data()
events = df[df["accel_mps2"] < -2.0].copy()
path = output_path("ex204_hard_braking.csv")
events.to_csv(path,index=False,encoding="utf-8-sig")
print("detected samples:", len(events))
print(events[["time_s","accel_mps2","event_label"]].head())
