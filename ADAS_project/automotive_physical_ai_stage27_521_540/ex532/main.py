import time
from common.adas_tb3_utils import *
world='<body name="stop_sign" pos="1.8 .8 .55"><geom type="cylinder" size=".25 .04" euler="90 0 0" rgba="1 .1 .1 1"/></body>'
mj,m,d=load(scene("ex532.xml",world))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); detected=x>.7; wheels(d,0,0) if detected else wheels(d,4,4); print("STOP" if detected else "SEARCH")
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
