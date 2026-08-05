import time,json
from common.viewer_utils import load,wheels,out
mj,m,d=load(); b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base"); o=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"obstacle"); rows=[]
with mj.viewer.launch_passive(m,d) as v:
 v.cam.type=mj.mjtCamera.mjCAMERA_TRACKING; v.cam.trackbodyid=b; v.cam.distance=3
 while v.is_running() and d.time<15:
  dist=float(((d.xpos[b]-d.xpos[o])**2).sum()**.5); wheels(d,0,0) if dist<.8 else wheels(d,7,7)
  mj.mj_step(m,d); rows.append(dist); v.sync(); time.sleep(m.opt.timestep)
r={"samples":len(rows),"min_distance":min(rows) if rows else None}; p=out("ex420_report.json"); p.write_text(json.dumps(r,indent=2)); print(r,p)
