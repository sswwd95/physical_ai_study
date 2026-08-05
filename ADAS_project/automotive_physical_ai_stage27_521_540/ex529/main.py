import time
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex529.xml",'<body name="lead" mocap="true" pos="2 0 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .2 .1 1"/></body>'))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<12:
  x,y,yaw=pose(d); dist=d.mocap_pos[0][0]-x; cmd=0 if dist<.45 else 2 if dist<1 else 4.5
  print("AEB_STOP" if cmd==0 else "AEB_BRAKE" if cmd==2 else "CRUISE"); wheels(d,cmd,cmd)
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
