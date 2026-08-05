import time
from common.ops import load,wheels
mj,m,d=load()
import numpy as np
from common.ops import xy,dist,Delay,save
b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base"); dock=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"dock"); q=Delay(20); rng=np.random.default_rng(42); rows=[]
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<22:
  p=xy(d,b); dd=dist(p,xy(d,dock)); gd=dist(p,(2,2)); des=(7,7)
  if gd<1.3:des=(-5,5)
  if dd<1.8:des=(3,3)
  if dd<.6:des=(0,0)
  app=q.push(des)
  if rng.random()<.1: app=(float(d.ctrl[0]),float(d.ctrl[1]))
  wheels(d,*app); mj.mj_step(m,d); rows.append([dd,gd,*d.ctrl[:2]]); v.sync(); time.sleep(m.opt.timestep)
r={"samples":len(rows),"min_dock":min(x[0] for x in rows) if rows else None}; print(r,save(r,"ex460.json"))
