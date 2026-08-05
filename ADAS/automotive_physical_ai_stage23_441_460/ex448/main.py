import time
from common.ops import load,wheels
mj,m,d=load()
from common.ops import Delay
q=Delay(30)
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<14:
  desired=(8,8) if d.time<5 else (-5,5) if d.time<10 else (0,0); wheels(d,*q.push(desired)); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
