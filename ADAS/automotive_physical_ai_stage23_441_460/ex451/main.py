import time
from common.ops import load,wheels
mj,m,d=load()
import numpy as np
bias=np.array([.08,-.04,.02]); samples=[]
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<10:
  mj.mj_step(m,d); measured=d.sensordata[7:10]+bias
  if d.time<3:samples.append(measured.copy())
  est=np.mean(samples,axis=0) if samples else np.zeros(3); print(measured-est); v.sync(); time.sleep(m.opt.timestep)
