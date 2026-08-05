import time
from common.viewer_utils import load
mj,m,d=load()
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<8:
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
 print(d.time)
