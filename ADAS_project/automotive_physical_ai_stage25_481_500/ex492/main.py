import time
from common.dynamics_utils import load_project,set_all,chassis_rpy
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        set_all(data,12); mujoco.mj_step(model,data)
        print("x",round(float(data.qpos[0]),2),"pitch",round(chassis_rpy(data)[1],3))
        viewer.sync(); time.sleep(model.opt.timestep)
