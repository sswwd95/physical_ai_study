import time
from common.ops import load,wheels
mj,m,d=load()
from common.ops import xy,dist
b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base"); dock=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"dock")
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<20:
  z=dist(xy(d,b),xy(d,dock)); cmd=7 if z>2 else 3 if z>.6 else 0; wheels(d,cmd,cmd); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
