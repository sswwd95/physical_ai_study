import time,math
from common.project_viewer_utils import load_project,pure_pursuit_command,set_wheels
mujoco,model,data,path=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING
    viewer.cam.trackbodyid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"base")
    viewer.cam.distance=3.5
    while viewer.is_running() and data.time<25:
        x,y=float(data.qpos[0]),float(data.qpos[1])
        qw,qx,qy,qz=data.qpos[3:7]
        yaw=math.atan2(2*(qw*qz+qx*qy),1-2*(qy*qy+qz*qz))
        left,right,_,target,_=pure_pursuit_command(path,x,y,yaw,.5,.8)
        set_wheels(data,left,right)
        data.mocap_pos[0]=[path.iloc[target]["x_m"],path.iloc[target]["y_m"],.08]
        mujoco.mj_step(model,data)
        viewer.sync()
        time.sleep(model.opt.timestep)
