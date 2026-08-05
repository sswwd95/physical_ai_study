from common.sync_utils import load_stream, nearest_merge, out
imu = load_stream("imu_50hz.csv")
wheel = load_stream("wheel_20hz.csv")
wheel["wheel_speed_mps"]=(wheel["wheel_left_mps"]+wheel["wheel_right_mps"])/2
m = nearest_merge(imu, wheel, tolerance=0.03).dropna().copy()
estimate = []
v = float(m["wheel_speed_mps"].iloc[0])
prev_t = float(m["timestamp_s"].iloc[0])
for _, r in m.iterrows():
    dt = float(r["timestamp_s"]-prev_t)
    predicted = v + float(r["imu_ax_mps2"])*dt
    v = 0.9*predicted + 0.1*float(r["wheel_speed_mps"])
    estimate.append(v)
    prev_t=float(r["timestamp_s"])
m["complementary_speed_mps"]=estimate
path=out("ex095_complementary_filter.csv")
m.to_csv(path,index=False)
print(m[["timestamp_s","wheel_speed_mps","complementary_speed_mps"]].head())
