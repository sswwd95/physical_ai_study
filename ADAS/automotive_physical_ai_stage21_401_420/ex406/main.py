from common.viewer_utils import load,run,wheels
mj,m,d=load()
def c(m,d):
 t=d.time; wheels(d,7,7) if t<4 else wheels(d,3,8) if t<8 else wheels(d,0,0)
with mj.viewer.launch_passive(m,d) as v: run(mj,m,d,v,12,c)
