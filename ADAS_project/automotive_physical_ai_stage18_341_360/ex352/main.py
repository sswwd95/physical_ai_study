import numpy as np
from common.safety_utils import load_data,output_path
df=load_data()
df["avoidance_yaw_rate_rps"]=np.where(
    df["distance_m"]<df["safe_distance_m"],
    np.clip(-0.05*df["obstacle_angle_deg"],-1.0,1.0),
    0.0
)
p=output_path("ex352_avoidance_yaw_rate.csv")
df[["time_s","obstacle_angle_deg","avoidance_yaw_rate_rps"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df["avoidance_yaw_rate_rps"].describe())
