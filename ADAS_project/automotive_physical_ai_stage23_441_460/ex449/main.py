import time
from common.ops import load,wheels
mj,m,d=load()
import numpy as np
rng=np.random.default_rng(8); applied=(0,0)
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  if rng.random()>.2: applied=(7,9)
  wheels(d,*applied); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
