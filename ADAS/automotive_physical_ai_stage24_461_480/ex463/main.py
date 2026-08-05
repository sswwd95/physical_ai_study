import time
from common.traffic_utils import load_project,set_ego,signal_phase
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        phase=signal_phase(data.time)
        x=float(data.qpos[0])
        cmd=0 if phase=="RED" and x>-1.5 else 7
        set_ego(data,cmd,cmd)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
