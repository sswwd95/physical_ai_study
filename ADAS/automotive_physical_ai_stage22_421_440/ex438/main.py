import time,numpy as np
from common.project_viewer_utils import load_project,set_wheels,body_distance
mujoco,model,data,path=load_project()
base=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"base")
obs=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"obstacle_1")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        raw=np.array([.8,.2])
        dist=body_distance(data,base,obs)
        safe=raw.copy()
        if dist<1.5:safe[0]=-.8
        set_wheels(data,8*safe[0]-4*safe[1],8*safe[0]+4*safe[1])
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
