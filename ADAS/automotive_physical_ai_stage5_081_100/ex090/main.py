from common.sync_utils import load_stream, out
df = load_stream("wheel_20hz.csv")
df["wheel_speed_fused_mps"] = (df["wheel_left_mps"] + df["wheel_right_mps"]) / 2
path = out("ex090_wheel_speed_fused.csv")
df.to_csv(path,index=False)
print(df[["timestamp_s","wheel_speed_fused_mps"]].head())
