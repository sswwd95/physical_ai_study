from common.sync_utils import load_stream, nearest_merge, out
wheel = load_stream("wheel_20hz.csv")
wheel["wheel_speed_mps"] = (wheel["wheel_left_mps"]+wheel["wheel_right_mps"])/2
gps = load_stream("gps_2hz.csv")
m = nearest_merge(wheel, gps, tolerance=0.26)
m["fused_speed_mps"] = 0.8*m["wheel_speed_mps"] + 0.2*m["gps_speed_mps"]
path = out("ex091_weighted_speed_fusion.csv")
m.to_csv(path,index=False)
print(m[["timestamp_s","wheel_speed_mps","gps_speed_mps","fused_speed_mps"]].dropna().head())
