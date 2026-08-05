from common.viewer_utils import load,run,wheels
mj,m,d=load(); cid=mj.mj_name2id(m,mj.mjtObj.mjOBJ_CAMERA,"overview")
with mj.viewer.launch_passive(m,d) as v:
 v.cam.type=mj.mjtCamera.mjCAMERA_FIXED; v.cam.fixedcamid=cid
 run(mj,m,d,v,10,lambda m,d:wheels(d,7,6))
