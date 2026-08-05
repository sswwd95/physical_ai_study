import numpy as np
from common.safety_utils import load_data,output_path
df=load_data()
margin=df["distance_m"]-df["safe_distance_m"]
df["speed_limit_mps"]=np.where(margin>=0,df["ego_speed_mps"],np.clip(df["ego_speed_mps"]+0.35*margin,0,df["ego_speed_mps"]))
p=output_path("ex354_safety_speed_limit.csv")
df[["time_s","distance_m","safe_distance_m","speed_limit_mps"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df["speed_limit_mps"].describe())
