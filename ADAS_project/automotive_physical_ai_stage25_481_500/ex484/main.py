import time
from common.dynamics_utils import load_project,set_all
mujoco,model,data,plan=load_project()
jids=[model.joint(n).id for n in ["fl_suspension","fr_suspension","rl_suspension","rr_suspension"]]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        if data.time>6:
            with viewer.lock():
                for jid in jids:model.jnt_stiffness[jid]=350
        set_all(data,10); mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
