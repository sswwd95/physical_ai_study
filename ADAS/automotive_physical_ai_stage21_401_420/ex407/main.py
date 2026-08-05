from common.viewer_utils import load,run,wheels
mj,m,d=load()
with mj.viewer.launch_passive(m,d) as v:
 v.cam.type=mj.mjtCamera.mjCAMERA_FREE; v.cam.lookat[:]=[1,0,.2]; v.cam.distance=5; v.cam.azimuth=135; v.cam.elevation=-25
 run(mj,m,d,v,10,lambda m,d:wheels(d,6,7))
