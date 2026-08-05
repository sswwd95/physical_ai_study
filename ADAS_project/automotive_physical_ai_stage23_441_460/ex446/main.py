import time
from common.ops import load,wheels
mj,m,d=load()
import numpy as np
rng=np.random.default_rng(21); last=np.zeros(m.nsensordata)
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  wheels(d,6,6); mj.mj_step(m,d)
  if rng.random()>.25:last=d.sensordata.copy()
  print(last); v.sync(); time.sleep(m.opt.timestep)
