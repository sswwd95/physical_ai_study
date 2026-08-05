import time
from common.ops import load,wheels
mj,m,d=load()
speeds=[4,7,10]; idx=0
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<15:
  idx=min(int(d.time//5),2); wheels(d,speeds[idx],speeds[idx]); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
