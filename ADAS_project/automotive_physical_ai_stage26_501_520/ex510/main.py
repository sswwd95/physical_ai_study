import time
from common.tb3_burger_utils import load_tb3,set_wheels,base_pose
mujoco,model,data,ids=load_tb3()
next_print=0
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<12:
        set_wheels(data,4,4)
        mujoco.mj_step(model,data)
        if data.time>=next_print:
            print(base_pose(data))
            next_print+=1
        viewer.sync()
        time.sleep(model.opt.timestep)
