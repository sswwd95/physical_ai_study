import time
from common.adas_tb3_utils import *
world='<body name="obstacle" pos="1.5 0 .15"><geom type="box" size=".2 .25 .15" rgba=".9 .2 .1 1"/></body>'
mj,m,d=load(scene("ex530.xml",world))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); wheels(d,2,5.5) if 1.5-x<.9 else wheels(d,4.5,4.5)
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
