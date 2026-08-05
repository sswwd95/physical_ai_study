import numpy as np
from common.safety_utils import load_data,output_path
df=load_data()
ratio=np.clip(df["distance_m"]/df["safe_distance_m"],0,1.5)
df["target_speed_mps"]=df["ego_speed_mps"]*np.clip(ratio,0,1)
df["decel_cmd_mps2"]=np.clip((df["target_speed_mps"]-df["ego_speed_mps"])/1.0,-4.0,0.0)
p=output_path("ex349_deceleration_command.csv")
df[["time_s","ego_speed_mps","target_speed_mps","decel_cmd_mps2"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df["decel_cmd_mps2"].describe())
