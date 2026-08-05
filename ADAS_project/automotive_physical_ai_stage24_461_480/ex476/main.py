import time
from common.traffic_utils import load_project,set_ego
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        x=float(data.qpos[0])
        cmd=3 if 1<x<4 else 7
        set_ego(data,cmd,cmd)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
