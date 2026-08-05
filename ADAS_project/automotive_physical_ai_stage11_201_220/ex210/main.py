from common.anomaly_utils import load_data, iqr_bounds, output_path
df = load_data()
flags = []
for col in ["accel_mps2","steering_deg","motor_current_a"]:
    low, high = iqr_bounds(df[col], 1.5)
    flags.append((df[col] < low) | (df[col] > high))
df["iqr_anomaly"] = flags[0] | flags[1] | flags[2]
path = output_path("ex210_iqr_anomalies.csv")
df[df["iqr_anomaly"]].to_csv(path,index=False,encoding="utf-8-sig")
print("detected:", int(df["iqr_anomaly"].sum()))
