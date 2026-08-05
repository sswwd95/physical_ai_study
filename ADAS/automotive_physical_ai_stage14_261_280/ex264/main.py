import numpy as np
from common.health_utils import load_data,output_path
df=load_data()
df["vibration_rms"]=np.sqrt(df["bearing_vibration_g"].pow(2).rolling(50,min_periods=1).mean())
p=output_path("ex264_bearing_vibration_rms.csv")
df[["time_s","bearing_vibration_g","vibration_rms"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df["vibration_rms"].tail())
