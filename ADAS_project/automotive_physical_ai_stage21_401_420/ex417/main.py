import time
from common.viewer_utils import load,wheels
mj,m,d=load(); nxt=0
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  wheels(d,6,8); mj.mj_step(m,d)
  if d.time>=nxt: print(d.time,d.sensordata.copy()); nxt+=1
  v.sync(); time.sleep(m.opt.timestep)
