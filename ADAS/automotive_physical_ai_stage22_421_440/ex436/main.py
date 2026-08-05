import time,math
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<16:
        risk=1/(1+math.exp(-(.45*data.time-4)))
        set_wheels(data,7*(1-risk),7*(1-risk))
        with viewer.lock():
            model.geom_rgba[gid]=[risk,1-risk,.1,1]
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
