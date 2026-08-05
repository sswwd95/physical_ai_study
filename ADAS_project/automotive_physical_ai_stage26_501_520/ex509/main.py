from common.tb3_burger_utils import load_tb3,realtime_loop,set_wheels
mujoco,model,data,ids=load_tb3()
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING
    viewer.cam.trackbodyid=ids["base_body"]
    viewer.cam.distance=1.8
    viewer.cam.azimuth=135
    viewer.cam.elevation=-25
    realtime_loop(mujoco,model,data,viewer,14,lambda m,d:set_wheels(d,3.5,5.0))
