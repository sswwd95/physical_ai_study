import time
from common.ops import load,wheels
mj,m,d=load()
cmds=[(6,6)]*250+[(3,8)]*250+[(0,0)]*150
with mj.viewer.launch_passive(m,d) as v:
 for c in cmds:
  if not v.is_running():break
  wheels(d,*c); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
print(d.qpos.copy())
