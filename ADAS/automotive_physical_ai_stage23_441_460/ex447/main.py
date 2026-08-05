import time
from common.ops import load,wheels
mj,m,d=load()
frozen=None
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  wheels(d,6,9); mj.mj_step(m,d); value=float(d.sensordata[-2])
  if d.time>5 and frozen is None:frozen=value
  print("used",frozen if frozen is not None else value); v.sync(); time.sleep(m.opt.timestep)
