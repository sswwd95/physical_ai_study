import time
from common.traffic_utils import load_project,set_ego,signal_phase
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        phase=signal_phase(data.time)
        time_to_change=5-(data.time%14) if phase=="RED" else 12-(data.time%14) if phase=="GREEN" else 14-(data.time%14)
        print({"phase":phase,"time_to_change":round(time_to_change,2)})
        set_ego(data,4 if phase=="RED" else 7,4 if phase=="RED" else 7)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
