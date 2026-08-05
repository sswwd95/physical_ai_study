import time
from common.traffic_utils import load_project,signal_phase
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        print("phase:",signal_phase(data.time))
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
