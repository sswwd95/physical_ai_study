import time
from common.traffic_utils import load_project,set_ego
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<16:
        with viewer.lock():
            intensity=max(.15,1-data.time/16)
            model.light_diffuse[0]=[intensity,intensity,intensity]
        set_ego(data,6,6)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
