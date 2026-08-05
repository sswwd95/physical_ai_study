import time
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex526.xml",'<body name="blind" mocap="true" pos="-.5 .8 .15"><geom type="box" size=".25 .15 .12" rgba="1 .4 .1 1"/></body>'))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<14:
  d.mocap_pos[0]=[-.5+.08*d.time,.8,.15]; x,y,yaw=pose(d); dx=d.mocap_pos[0][0]-x; dy=d.mocap_pos[0][1]-y
  print("BLIND_SPOT_WARNING" if -1.2<dx<.5 and abs(dy)<1 else "CLEAR")
  wheels(d,4,4); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
