import time
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex523.xml",'<geom type="box" pos="3 .6 .01" size="8 .025 .01" rgba="1 1 1 1"/><geom type="box" pos="3 -.6 .01" size="8 .025 .01" rgba="1 1 1 1"/>'))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<14:
  x,y,yaw=pose(d); c=max(-2,min(2,-2.5*y-1.2*yaw)); wheels(d,4-c,4+c)
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
