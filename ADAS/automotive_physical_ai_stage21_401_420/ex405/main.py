from common.viewer_utils import load,run,wheels
mj,m,d=load()
with mj.viewer.launch_passive(m,d) as v: run(mj,m,d,v,10,lambda m,d:wheels(d,-5,5))
