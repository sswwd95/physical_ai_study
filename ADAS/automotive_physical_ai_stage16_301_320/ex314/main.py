import numpy as np, pandas as pd
from common.control_utils import output_path
dt=.05; y=0.8; yaw=0.0; speed=.3; kp=1.4
rows=[]
for k in range(240):
    yaw_rate=np.clip(-kp*y,-1.2,1.2)
    yaw += yaw_rate*dt
    y += speed*np.sin(yaw)*dt
    rows.append([k*dt,y,yaw,yaw_rate])
df=pd.DataFrame(rows,columns=["time_s","lateral_error_m","yaw_rad","yaw_rate_cmd"])
p=output_path("ex314_lateral_error_control.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print("final error:",df["lateral_error_m"].iloc[-1])
