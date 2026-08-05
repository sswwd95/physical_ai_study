import numpy as np, pandas as pd, json
from common.sync_utils import load_stream, nearest_merge, out
grid=pd.DataFrame({"timestamp_s":np.arange(0,90,0.1)})
imu=load_stream("imu_50hz.csv")
wheel=load_stream("wheel_20hz.csv")
wheel["wheel_speed_mps"]=(wheel["wheel_left_mps"]+wheel["wheel_right_mps"])/2
rng=load_stream("range_10hz.csv")
gps=load_stream("gps_2hz.csv")
m=nearest_merge(grid,imu,0.03)
m=nearest_merge(m,wheel[["timestamp_s","wheel_speed_mps"]],0.03)
m=nearest_merge(m,rng,0.06)
m=nearest_merge(m,gps,0.26)
m["gps_speed_mps"]=m["gps_speed_mps"].interpolate().bfill().ffill()
m["fused_speed_mps"]=0.85*m["wheel_speed_mps"]+0.15*m["gps_speed_mps"]
m["ttc_s"]=(m["front_distance_m"]/m["fused_speed_mps"].clip(lower=0.5)).clip(upper=30)
csv_path=out("ex100_fused_sensor_dataset.csv")
m.to_csv(csv_path,index=False)
summary={
 "rows":len(m),
 "remaining_missing":int(m.isna().sum().sum()),
 "mean_fused_speed_mps":float(m["fused_speed_mps"].mean()),
 "minimum_ttc_s":float(m["ttc_s"].min())
}
json_path=out("ex100_summary.json")
json_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
print(summary)
print("saved:",csv_path,json_path)
