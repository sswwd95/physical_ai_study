import time,math
from common.adas_tb3_utils import *
world='<body name="rear" mocap="true" pos="-1.5 -2 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .1 .6 1"/></body>'
mj,m,d=load(scene("ex527.xml",world))
with mj.viewer.launch_passive(m,d) as v:
 while v.is_running() and d.time<14:
  d.mocap_pos[0]=[-1.5,-2+.22*d.time,.15]; x,y,yaw=pose(d); r=math.hypot(d.mocap_pos[0][0]-x,d.mocap_pos[0][1]-y)
  print("RCCW" if r<1.2 else "CLEAR"); wheels(d,-3,-3); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
