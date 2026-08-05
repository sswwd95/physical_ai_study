import time
from common.viewer_utils import load
mj,m,d=load()
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<8:
  mj.mj_step(m,d)
  if 3<d.time<3.02:
   with v.lock(): d.qpos[0]=0; d.qpos[1]=1; mj.mj_forward(m,d)
  v.sync(); time.sleep(m.opt.timestep)
