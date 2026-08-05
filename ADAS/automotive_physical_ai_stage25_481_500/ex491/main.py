import time,math
from common.dynamics_utils import load_project,set_all,suspension_positions
mujoco,model,data,plan=load_project()
jid=model.joint("payload_x").id
adr=model.jnt_qposadr[jid]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        with viewer.lock():
            data.qpos[adr]=.18*math.sin(data.time*.5)
            mujoco.mj_forward(model,data)
        set_all(data,7); mujoco.mj_step(model,data)
        print(suspension_positions(model,data))
        viewer.sync(); time.sleep(model.opt.timestep)
