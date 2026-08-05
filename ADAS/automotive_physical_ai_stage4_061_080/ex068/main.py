from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
df["is_stop"] = df["speed_mps"] < 0.5
df["segment_id"] = (df["is_stop"] != df["is_stop"].shift()).cumsum()
segments = (
    df[df["is_stop"]]
    .groupby("segment_id")
    .agg(start_s=("time_s", "min"), end_s=("time_s", "max"), samples=("time_s", "size"))
)
segments["duration_s"] = segments["end_s"] - segments["start_s"] + 0.1
segments = segments[segments["duration_s"] >= 1.0]
path = output_path("ex068_stop_segments.csv")
segments.to_csv(path, encoding="utf-8-sig")
print(segments)
print(f"saved: {path}")
