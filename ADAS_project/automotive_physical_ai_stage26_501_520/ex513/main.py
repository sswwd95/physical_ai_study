import time
from common.tb3_burger_utils import load_tb3,set_wheels
mujoco,model,data,ids=load_tb3()
print("actuator ctrlrange:",model.actuator_ctrlrange.copy())
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<10:
        set_wheels(data,100,-100)
        mujoco.mj_step(model,data)
        print("applied:",data.ctrl.copy())
        viewer.sync()
        time.sleep(model.opt.timestep)
