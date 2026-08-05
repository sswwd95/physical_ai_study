import time
from common.ops import load,wheels
mj,m,d=load()
import pandas as pd
from common.ops import out
rows=[]
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  wheels(d,7,7); mj.mj_step(m,d); e=float((d.qvel[-2]+d.qvel[-1])/2); rows.append([d.time,e*.06,e*.055]); v.sync(); time.sleep(m.opt.timestep)
p=out("ex450.csv"); pd.DataFrame(rows,columns=["time","nominal","wrong"]).to_csv(p,index=False); print(p)
