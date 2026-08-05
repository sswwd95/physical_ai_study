from common.anomaly_utils import load_data, output_path
df = load_data()
df["anomaly_flag"] = (
    (df["accel_mps2"].abs() > 1.8) |
    (df["steering_deg"].abs() > 15) |
    (df["ttc_s"] < 2) |
    (df["motor_current_a"] > 7)
)
df["group"] = (df["anomaly_flag"] != df["anomaly_flag"].shift()).cumsum()
segments = (
    df[df["anomaly_flag"]]
    .groupby("group")
    .agg(start_s=("time_s","min"), end_s=("time_s","max"), samples=("time_s","size"))
)
segments["duration_s"] = segments["end_s"] - segments["start_s"] + 0.1
path = output_path("ex213_anomaly_segments.csv")
segments.to_csv(path,encoding="utf-8-sig")
print(segments)
