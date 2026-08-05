import time
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex538.xml",'<body name="lead" mocap="true" pos="2 0 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .2 .1 1"/></body>'))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); dist=d.mocap_pos[0][0]-x; w=[]
  if dist<.5:w.append(("AEB",3))
  if abs(y)>.45:w.append(("LDW",2))
  if d.time>9:w.append(("DAW",1))
  active=max(w,key=lambda z:z[1])[0] if w else "NORMAL"; print(active); wheels(d,0,0) if active=="AEB" else wheels(d,4,4)
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
