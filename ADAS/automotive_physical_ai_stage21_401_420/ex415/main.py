import time
from common.viewer_utils import load,wheels
mj,m,d=load(); paused=False
def key(k):
 global paused
 if k==32: paused=not paused
with mj.viewer.launch_passive(m,d,key_callback=key) as v:
 while v.is_running():
  if not paused: wheels(d,6,7); mj.mj_step(m,d)
  v.sync(); time.sleep(m.opt.timestep)
