import time
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        t=data.time
        if t<5:set_wheels(data,6,6)
        elif t<8:set_wheels(data,14,14)
        elif t<12:set_wheels(data,-12,12)
        elif t<16:set_wheels(data,3,10)
        else:set_wheels(data,0,0)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
