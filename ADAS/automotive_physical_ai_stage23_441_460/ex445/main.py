import time
from common.ops import load,wheels
mj,m,d=load()
import numpy as np
rng=np.random.default_rng(42)
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  wheels(d,6,7); mj.mj_step(m,d); print(d.sensordata+rng.normal(0,.03,len(d.sensordata))); v.sync(); time.sleep(m.opt.timestep)
