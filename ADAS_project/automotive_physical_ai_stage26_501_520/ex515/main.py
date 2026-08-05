import time
from common.tb3_burger_utils import load_tb3,set_wheels
mujoco,model,data,ids=load_tb3()
left_body=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"wheel_left")
right_body=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"wheel_right")
wheel_geoms=[i for i in range(model.ngeom) if model.geom_bodyid[i] in (left_body,right_body)]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<16:
        if data.time>7:
            with viewer.lock():
                for gid in wheel_geoms:
                    model.geom_friction[gid,0]=0.2
        set_wheels(data,5,5)
        mujoco.mj_step(model,data)
        viewer.sync()
        time.sleep(model.opt.timestep)
