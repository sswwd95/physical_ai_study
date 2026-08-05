import time
from common.ops import load,wheels
mj,m,d=load()
from common.ops import xy,dist
b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base")
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<16:
  wheels(d,-5,5) if dist(xy(d,b),(2,2))<1.3 else wheels(d,7,8); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
