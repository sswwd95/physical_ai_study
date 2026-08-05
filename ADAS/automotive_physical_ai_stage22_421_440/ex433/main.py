import time
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<16:
        voltage=12.6-.08*data.time
        cmd=8 if voltage>12 else 5 if voltage>11.5 else 2
        set_wheels(data,cmd,cmd)
        print("voltage",round(voltage,2),"cmd",cmd)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
