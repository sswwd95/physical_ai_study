import time
from common.tb3_burger_utils import load_tb3,set_wheels
mujoco,model,data,ids=load_tb3()
left_dof=model.jnt_dofadr[ids["wheel_left_joint"]]
right_dof=model.jnt_dofadr[ids["wheel_right_joint"]]
next_print=0
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<12:
        set_wheels(data,3.0,5.0)
        mujoco.mj_step(model,data)
        if data.time>=next_print:
            print("left:",data.qvel[left_dof],"right:",data.qvel[right_dof])
            next_print+=1
        viewer.sync()
        time.sleep(model.opt.timestep)
