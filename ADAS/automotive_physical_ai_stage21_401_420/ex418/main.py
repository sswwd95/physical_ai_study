import time,pandas as pd
from common.viewer_utils import load,wheels,out
mj,m,d=load(); rows=[]
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<8:
  wheels(d,6,7); mj.mj_step(m,d); rows.append([d.time,*d.qpos[:3],*d.ctrl[:2]]); v.sync(); time.sleep(m.opt.timestep)
p=out("ex418_log.csv"); pd.DataFrame(rows,columns=["time","x","y","z","left","right"]).to_csv(p,index=False); print(p)
