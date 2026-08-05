import time
from common.viewer_utils import load,wheels
mj,m,d=load(); cmd=[0,0]
def key(k):
 if k in (87,119): cmd[:]=[7,7]
 elif k in (65,97): cmd[:]=[-4,4]
 elif k in (68,100): cmd[:]=[4,-4]
 elif k in (83,115): cmd[:]=[0,0]
with mj.viewer.launch_passive(m,d,key_callback=key) as v:
 while v.is_running(): wheels(d,*cmd); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
