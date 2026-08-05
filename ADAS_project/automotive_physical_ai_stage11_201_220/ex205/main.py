from common.anomaly_utils import load_data, output_path
df = load_data()
events = df[df["steering_deg"].abs() > 15].copy()
path = output_path("ex205_sharp_turn.csv")
events.to_csv(path,index=False,encoding="utf-8-sig")
print("detected samples:", len(events))
print(events[["time_s","steering_deg","event_label"]].head())
