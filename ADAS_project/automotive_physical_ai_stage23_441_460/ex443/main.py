import time
from common.ops import load,wheels
mj,m,d=load()
import numpy as np
g=mj.mj_name2id(m,mj.mjtObj.mjOBJ_GEOM,"floor"); rng=np.random.default_rng(42); nxt=0
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<15:
  if d.time>=nxt:
   with v.lock(): m.geom_friction[g,0]=float(rng.uniform(.3,1.0))
   nxt+=3
  wheels(d,8,8); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
