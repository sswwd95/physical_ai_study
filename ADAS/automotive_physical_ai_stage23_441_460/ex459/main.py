import time
from common.ops import load,wheels
mj,m,d=load()
import pandas as pd
from common.ops import out
rows=[]
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  wheels(d,7,8); mj.mj_step(m,d); pred=.35*d.time; actual=float(d.qpos[0]); rows.append([d.time,pred,actual,actual-pred]); v.sync(); time.sleep(m.opt.timestep)
p=out("ex459.csv"); pd.DataFrame(rows,columns=["time","pred","actual","error"]).to_csv(p,index=False); print(p)
