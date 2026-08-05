import time
from common.project_viewer_utils import load_project,set_wheels,body_distance
mujoco,model,data,path=load_project()
base=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"base")
obs=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"obstacle_1")
prev=body_distance(data,base,obs)
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<16:
        dist=body_distance(data,base,obs)
        closing=max(0,(prev-dist)/model.opt.timestep)
        ttc=dist/max(closing,.01)
        set_wheels(data,0,0) if ttc<1.5 else set_wheels(data,8,8)
        prev=dist
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
