import pandas as pd
from common.control_utils import PID, output_path
dt=.02; v=w=0.0
vp=PID(1.5,.7,.08,2.0,2.0); wp=PID(2.0,.8,.12,2.5,2.0)
rows=[]
for k in range(int(10/dt)):
    t=k*dt
    vt=.25 if t<6 else .12
    wt=.0 if t<3 else (.6 if t<7 else -.4)
    vu,ve,_,_=vp.update(vt,v,dt); wu,we,_,_=wp.update(wt,w,dt)
    v+=(vu-v)/.5*dt; w+=(wu-w)/.35*dt
    rows.append([t,vt,v,wt,w,vu,wu,ve,we])
df=pd.DataFrame(rows,columns=["time_s","target_v","v","target_w","w","v_ctrl","w_ctrl","v_error","w_error"])
p=output_path("ex315_combined_twist_control.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print(df.tail())
