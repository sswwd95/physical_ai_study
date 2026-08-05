import time
from common.viewer_utils import load,wheels
mj,m,d=load(); reset=False
def key(k):
 global reset
 if k in (82,114): reset=True
with mj.viewer.launch_passive(m,d,key_callback=key) as v:
 while v.is_running():
  if reset:
   with v.lock(): mj.mj_resetData(m,d); mj.mj_forward(m,d)
   reset=False
  wheels(d,6,6); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
