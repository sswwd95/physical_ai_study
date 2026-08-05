import time
from common.dynamics_utils import load_project,set_all,suspension_positions
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<12:
        set_all(data,10); mujoco.mj_step(model,data)
        if int(data.time)%1==0 and data.time-int(data.time)<.01:
            print(suspension_positions(model,data))
        viewer.sync(); time.sleep(model.opt.timestep)
