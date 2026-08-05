import time,math
from common.project_viewer_utils import *
mujoco,model,data,path=load_project()
gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<22:
        x,y=float(data.qpos[0]),float(data.qpos[1])
        qw,qx,qy,qz=data.qpos[3:7]
        yaw=math.atan2(2*(qw*qz+qx*qy),1-2*(qy*qy+qz*qz))
        left,right,idx,target,_=pure_pursuit_command(path,x,y,yaw,.5,.8)
        error=abs(signed_cross_track_error(path,idx,x,y))
        set_wheels(data,left,right)
        with viewer.lock():
            model.geom_rgba[gid]=[min(1,error),max(0,1-error),.1,1]
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
