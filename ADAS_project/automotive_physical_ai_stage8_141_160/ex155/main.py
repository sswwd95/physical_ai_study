from common.sensor_utils import load_data, output_path
df = load_data()
df["speed_error_mps"] = df["encoder_speed_mps"] - df["true_speed_mps"]
df["slip_detected"] = df["speed_error_mps"].abs() > 0.03
events = df[df["slip_detected"]][["time_s","true_speed_mps","encoder_speed_mps","speed_error_mps","slip_flag"]]
path = output_path("ex155_slip_events.csv")
events.to_csv(path,index=False,encoding="utf-8-sig")
print("detected samples:", len(events))
print("true slip samples:", int(df["slip_flag"].sum()))
print("saved:", path)
