import time
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex524.xml",'<geom type="box" pos="3 .6 .01" size="8 .025 .01" rgba="1 1 1 1"/><geom type="box" pos="3 -.6 .01" size="8 .025 .01" rgba="1 1 1 1"/>'))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); print("LDW" if abs(y)>.45 else "NORMAL"); wheels(d,3,5)
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
