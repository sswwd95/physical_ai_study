import time
from common.adas_tb3_utils import *
world='<geom type="box" pos="-1.5 .55 .02" size=".8 .03 .02" rgba=".2 .7 1 1"/><geom type="box" pos="-1.5 -.55 .02" size=".8 .03 .02" rgba=".2 .7 1 1"/>'
mj,m,d=load(scene("ex537.xml",world))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<16:
  t=d.time
  if t<4:wheels(d,-3,-3)
  elif t<8:wheels(d,-2,-4)
  elif t<12:wheels(d,-4,-2)
  else:wheels(d,0,0)
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
