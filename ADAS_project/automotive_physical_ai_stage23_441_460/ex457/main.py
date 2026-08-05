import time
from common.ops import load,wheels
mj,m,d=load()
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<18:
  t=d.time; cmd=(0,0) if t<3 else (7,7) if t<9 else (-4,4) if t<13 else (5,6) if t<17 else (0,0); wheels(d,*cmd); print(t,cmd); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
