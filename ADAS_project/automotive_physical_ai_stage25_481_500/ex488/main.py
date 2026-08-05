import time
from common.dynamics_utils import load_project,set_all,chassis_rpy
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<10:
        set_all(data,0 if data.time<2 else 18)
        mujoco.mj_step(model,data)
        print("pitch",round(chassis_rpy(data)[1],4))
        viewer.sync(); time.sleep(model.opt.timestep)
