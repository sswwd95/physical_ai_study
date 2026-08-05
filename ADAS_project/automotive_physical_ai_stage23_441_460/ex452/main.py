import time
from common.ops import load,wheels
mj,m,d=load()
checkpoint=None; restored=False
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<14:
  wheels(d,7,8); mj.mj_step(m,d)
  if d.time>4 and checkpoint is None: checkpoint=(d.qpos.copy(),d.qvel.copy(),d.time)
  if d.time>9 and not restored:
   with v.lock(): d.qpos[:]=checkpoint[0]; d.qvel[:]=checkpoint[1]; d.time=checkpoint[2]; mj.mj_forward(m,d)
   restored=True
  v.sync(); time.sleep(m.opt.timestep)
