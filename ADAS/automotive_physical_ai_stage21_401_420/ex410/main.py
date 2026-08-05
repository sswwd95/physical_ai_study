from common.viewer_utils import load,run,wheels
mj,m,d=load()
with mj.viewer.launch_passive(m,d) as v:
 v.opt.flags[mj.mjtVisFlag.mjVIS_CONTACTPOINT]=True; v.opt.flags[mj.mjtVisFlag.mjVIS_CONTACTFORCE]=True
 run(mj,m,d,v,10,lambda m,d:wheels(d,8,8))
