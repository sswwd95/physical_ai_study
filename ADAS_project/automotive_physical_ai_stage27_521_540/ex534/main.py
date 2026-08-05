import time,math
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex534.xml"))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<16:
  attention=.5+.5*math.sin(d.time*.5); warning=attention<.4; wheels(d,2,2) if warning else wheels(d,4,4)
  print("DAW" if warning else "ATTENTIVE"); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
