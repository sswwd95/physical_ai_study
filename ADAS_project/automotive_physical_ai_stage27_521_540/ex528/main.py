import time
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex528.xml",'<body name="lead" mocap="true" pos="2 0 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .2 .1 1"/></body>')); prev=2
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); dist=d.mocap_pos[0][0]-x; closing=max(0,(prev-dist)/m.opt.timestep); ttc=dist/max(closing,.01)
  if ttc<2: print("FCW",round(ttc,2))
  wheels(d,4.5,4.5); prev=dist; mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
