import pandas as pd
from common.control_utils import PID, output_path
dt=.02; left=right=0.0
lp=PID(1.4,.7,0,20,10); rp=PID(1.4,.7,0,20,10)
rows=[]
for k in range(int(6/dt)):
    lu,le,_,_=lp.update(6.0,left,dt)
    ru,re,_,_=rp.update(8.0,right,dt)
    left += (lu-left)/.35*dt
    right += (ru-right)/.35*dt
    rows.append([k*dt,left,right,lu,ru,le,re])
df=pd.DataFrame(rows,columns=["time_s","left_rad_s","right_rad_s","left_ctrl","right_ctrl","left_error","right_error"])
p=output_path("ex312_dual_wheel_pi.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print(df.tail())
