import time,math
from common.dynamics_utils import load_project,set_drive
mujoco,model,data,plan=load_project()
trailer=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"trailer")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        diff=6*math.sin(data.time*1.3)
        set_drive(data,12-diff,12+diff,12-diff,12+diff)
        mujoco.mj_step(model,data)
        print("trailer_pos",data.xpos[trailer].copy())
        viewer.sync(); time.sleep(model.opt.timestep)
