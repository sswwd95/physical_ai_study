import time
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex533.xml"))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<14:
  ambient=max(.1,1-d.time/14); high=ambient<.35
  with v.lock(): m.light_diffuse[-1]=[1,1,1] if high else [.35,.35,.35]
  print("HIGH_BEAM" if high else "LOW_BEAM"); wheels(d,4,4); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
