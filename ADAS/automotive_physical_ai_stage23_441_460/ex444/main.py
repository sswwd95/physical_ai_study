import time
from common.ops import load,wheels
mj,m,d=load()
import numpy as np
g=mj.mj_name2id(m,mj.mjtObj.mjOBJ_GEOM,"chassis"); rng=np.random.default_rng(7)
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  if int(d.time)%3==0 and d.time-int(d.time)<.02:
   with v.lock(): m.geom_rgba[g]=[rng.random(),rng.random(),rng.random(),1]
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
