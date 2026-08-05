import time,numpy as np
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
def policy(obs):
    x,y,yaw,speed,dist=obs
    throttle=.7 if dist>1.5 else -.8
    steering=np.clip(-.8*y-.5*yaw,-1,1)
    return throttle,steering
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        x,y=float(data.qpos[0]),float(data.qpos[1])
        speed=float(np.linalg.norm(data.qvel[:2]))
        obs=[x,y,0.0,speed,3.0-x]
        throttle,steering=policy(obs)
        set_wheels(data,8*throttle-4*steering,8*throttle+4*steering)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
