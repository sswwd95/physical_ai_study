import time,pandas as pd
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex539.xml",'<body name="lead" mocap="true" pos="2 0 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .2 .1 1"/></body>')); rows=[]
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); dist=d.mocap_pos[0][0]-x; event="AEB" if dist<.5 else "LDW" if abs(y)>.45 else "NONE"; cmd=0 if event=="AEB" else 4
  wheels(d,cmd,cmd); rows.append([d.time,x,y,yaw,dist,event,cmd]); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
p=out("ex539_adas_events.csv"); pd.DataFrame(rows,columns=["time_s","x","y","yaw","distance","event","cmd"]).to_csv(p,index=False); print(p)
