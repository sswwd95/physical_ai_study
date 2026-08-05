import time,numpy as np
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        set_wheels(data,12,5 if data.time>6 else 12)
        mujoco.mj_step(model,data)
        slip=min(1.0,abs(data.qvel[-2]-data.qvel[-1])/12)
        with viewer.lock():
            model.geom_rgba[gid]=[slip,1-slip,.15,1]
        viewer.sync()
        time.sleep(model.opt.timestep)
