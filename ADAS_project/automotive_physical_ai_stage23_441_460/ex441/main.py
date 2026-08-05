import time
from common.ops import load,wheels
mj,m,d=load()
print("mass",m.body_mass.sum(),"timestep",m.opt.timestep)
mj.viewer.launch(m,d)
