import time
from common.ops import load,wheels
mj,m,d=load()
from common.ops import xy,dist
b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base"); target=(3,-2)
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<18:
  wheels(d,0,0) if dist(xy(d,b),target)<.5 else wheels(d,-5,-6); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
