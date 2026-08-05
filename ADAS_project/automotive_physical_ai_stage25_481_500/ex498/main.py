import time,math
from common.dynamics_utils import load_project,set_drive,chassis_rpy
mujoco,model,data,plan=load_project()
gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis_geom")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        diff=7*math.sin(data.time*1.5)
        set_drive(data,13-diff,13+diff,13-diff,13+diff)
        mujoco.mj_step(model,data)
        roll=abs(chassis_rpy(data)[0]); risk=min(1,roll/.5)
        with viewer.lock(): model.geom_rgba[gid]=[risk,1-risk,.1,1]
        viewer.sync(); time.sleep(model.opt.timestep)
