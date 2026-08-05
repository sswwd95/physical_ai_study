import time,math
from common.viewer_utils import load
mj,m,d=load()
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  d.mocap_pos[0]=[math.cos(d.time),math.sin(d.time),.1]; mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
