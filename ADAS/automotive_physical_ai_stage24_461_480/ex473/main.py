import time
from common.traffic_utils import load_project,set_ego
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        x=float(data.qpos[0])
        set_ego(data,3,8) if 1.5<x<3.5 else set_ego(data,7,7)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
