import time
from common.adas_tb3_utils import *
world='<body name="wall" pos="-1.5 0 .3"><geom type="box" size=".15 1 .3" rgba=".6 .6 .6 1"/></body>'
mj,m,d=load(scene("ex536.xml",world))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); distance=abs(x+1.5); wheels(d,-3,-3) if distance>.35 else wheels(d,0,0); print("PDW",round(distance,2))
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
