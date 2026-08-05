import time
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT]=True
    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTFORCE]=True
    while viewer.is_running() and data.time<12:
        if data.time<5:set_wheels(data,10,10)
        else:set_wheels(data,15,4)
        mujoco.mj_step(model,data)
        viewer.sync()
        time.sleep(model.opt.timestep)
