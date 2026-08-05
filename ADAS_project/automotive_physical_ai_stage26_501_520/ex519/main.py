import time
from common.tb3_burger_utils import load_tb3,set_wheels
mujoco,model,data,ids=load_tb3()
reset_done=False
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        set_wheels(data,4,5)
        mujoco.mj_step(model,data)
        if data.time>7 and not reset_done:
            with viewer.lock():
                mujoco.mj_resetData(model,data)
                mujoco.mj_forward(model,data)
            reset_done=True
            print("state reset completed")
        viewer.sync()
        time.sleep(model.opt.timestep)
