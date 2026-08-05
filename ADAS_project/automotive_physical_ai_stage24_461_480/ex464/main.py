import time
from common.traffic_utils import load_project,set_ego,signal_phase
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        phase=signal_phase(data.time); x=float(data.qpos[0])
        distance_to_line=max(0,-x)
        cmd=3 if phase=="YELLOW" and distance_to_line>1.5 else 7
        set_ego(data,cmd,cmd)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
