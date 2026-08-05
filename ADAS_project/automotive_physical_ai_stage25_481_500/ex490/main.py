import time,math
from common.dynamics_utils import load_project,set_all
mujoco,model,data,plan=load_project()
jid=model.joint("payload_y").id
adr=model.jnt_qposadr[jid]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        with viewer.lock():
            data.qpos[adr]=.12*math.sin(data.time*.6)
            mujoco.mj_forward(model,data)
        set_all(data,8); mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
