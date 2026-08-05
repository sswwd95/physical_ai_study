from common.adas_tb3_utils import *
p=scene("ex521.xml",'<geom type="box" pos="3 .6 .01" size="8 .025 .01" rgba="1 1 1 1"/><geom type="box" pos="3 -.6 .01" size="8 .025 .01" rgba="1 1 1 1"/>'); mj,m,d=load(p); print(p,m.nbody,m.nu); mj.viewer.launch(m,d)
