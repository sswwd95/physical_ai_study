from common.viewer_utils import load,run,wheels
mj,m,d=load(); bid=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base")
with mj.viewer.launch_passive(m,d) as v:
 v.cam.type=mj.mjtCamera.mjCAMERA_TRACKING; v.cam.trackbodyid=bid; v.cam.distance=3
 run(mj,m,d,v,10,lambda m,d:wheels(d,6,8))
