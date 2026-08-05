import time
from common.dynamics_utils import load_project,set_drive
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<12:
        set_drive(data,8,10,8,10)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
