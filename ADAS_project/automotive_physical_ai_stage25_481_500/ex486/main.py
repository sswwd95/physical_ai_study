import time
from common.dynamics_utils import load_project,set_all,chassis_rpy
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        set_all(data,10); mujoco.mj_step(model,data)
        r,p,y=chassis_rpy(data)
        print("roll",round(r,3),"pitch",round(p,3))
        viewer.sync(); time.sleep(model.opt.timestep)
