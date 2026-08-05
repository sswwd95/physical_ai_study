import time,math
from common.viewer_utils import load
mj,m,d=load(); gid=mj.mj_name2id(m,mj.mjtObj.mjOBJ_GEOM,"chassis")
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  mj.mj_step(m,d); x=.5+.5*math.sin(d.time*2)
  with v.lock(): m.geom_rgba[gid]=[x,.2,1-x,1]
  v.sync(); time.sleep(m.opt.timestep)
