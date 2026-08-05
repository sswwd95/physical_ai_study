import time,math
from common.dynamics_utils import load_project,set_drive,chassis_rpy
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        diff=5*math.sin(data.time*1.4)
        set_drive(data,10-diff,10+diff,10-diff,10+diff)
        mujoco.mj_step(model,data)
        print("roll",round(chassis_rpy(data)[0],4))
        viewer.sync(); time.sleep(model.opt.timestep)
