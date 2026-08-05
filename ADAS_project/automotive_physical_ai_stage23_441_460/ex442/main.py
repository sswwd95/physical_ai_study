import time
from common.ops import load,wheels
mj,m,d=load()
pid=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"payload")
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<14:
  if d.time>6:
   with v.lock(): m.body_mass[pid]=1.2; mj.mj_setConst(m,d)
  wheels(d,7,7); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
