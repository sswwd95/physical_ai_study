from common.sync_utils import load_stream, out
df = load_stream("imu_50hz.csv")
df["bin"] = (df["timestamp_s"] / 0.1).astype(int)
down = df.groupby("bin").agg(timestamp_s=("timestamp_s","mean"), imu_ax_mps2=("imu_ax_mps2","mean"), imu_gyroz_rps=("imu_gyroz_rps","mean"))
path = out("ex084_imu_10hz.csv")
down.to_csv(path, index=False)
print(down.head())
print("saved:", path)
