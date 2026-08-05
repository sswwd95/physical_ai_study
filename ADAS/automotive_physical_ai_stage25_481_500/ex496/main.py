import time,math
from common.dynamics_utils import load_project,set_drive
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        diff=3*math.sin(data.time*.7)
        set_drive(data,8-diff,8+diff,8-diff,8+diff)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
