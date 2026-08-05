import time
from collections import deque
from common.traffic_utils import load_project,set_ego,signal_phase
mujoco,model,data,plan=load_project()
queue=deque(["RED"]*50,maxlen=51)
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        queue.append(signal_phase(data.time))
        delayed=queue[0]
        set_ego(data,0,0) if delayed=="RED" else set_ego(data,7,7)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
