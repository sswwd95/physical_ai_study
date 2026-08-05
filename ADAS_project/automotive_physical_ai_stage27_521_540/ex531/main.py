import time
from common.adas_tb3_utils import *
world='<body name="sign" pos="1.5 .9 .5"><geom type="cylinder" size=".25 .04" euler="90 0 0" rgba="1 1 1 1"/></body>'
mj,m,d=load(scene("ex531.xml",world))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); limit=3 if x>1 else 5.5; wheels(d,limit,limit); print("LIMIT",limit)
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
