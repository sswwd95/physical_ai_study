from common.data_utils import load_vehicle_data, output_path

df = load_vehicle_data()
df["is_turn"] = df["steering_deg"].abs() >= 8
df["turn_group"] = (df["is_turn"] != df["is_turn"].shift()).cumsum()
turns = (
    df[df["is_turn"]]
    .groupby("turn_group")
    .agg(start_s=("time_s", "min"), end_s=("time_s", "max"),
         max_abs_steering=("steering_deg", lambda s: s.abs().max()),
         mean_yaw_rate=("yaw_rate_rps", "mean"))
)
turns["duration_s"] = turns["end_s"] - turns["start_s"] + 0.1
turns = turns[turns["duration_s"] >= 0.5]
path = output_path("ex071_turn_segments.csv")
turns.to_csv(path, encoding="utf-8-sig")
print(turns)
print(f"saved: {path}")
