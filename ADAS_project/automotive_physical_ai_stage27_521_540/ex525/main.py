import time
from common.adas_tb3_utils import *
world='<body name="blind" mocap="true" pos="-.5 .8 .15"><geom type="box" size=".25 .15 .12" rgba="1 .4 .1 1"/></body>'; mj,m,d=load(scene("ex525.xml",world))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  side=abs(float(d.mocap_pos[0][1]-d.qpos[1])); ok=side>.8; print("CHANGE_OK" if ok else "BLOCKED")
  wheels(d,4,5 if ok else 4); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
