import time
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex535.xml"))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<16:
  drowsy=d.time>8; wheels(d,0,0) if drowsy else wheels(d,4,4); print("MINIMUM_RISK_STOP" if drowsy else "NORMAL")
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
