import time
from common.traffic_utils import load_project,set_ego
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<16:
        visibility=max(5,25-1.2*data.time)
        cmd=7 if visibility>15 else 4 if visibility>8 else 2
        set_ego(data,cmd,cmd)
        print("visibility_m",round(visibility,1))
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
