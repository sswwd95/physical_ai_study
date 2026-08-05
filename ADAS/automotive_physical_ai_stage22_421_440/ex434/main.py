import time
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        temp=45+1.8*data.time
        cmd=8 if temp<65 else 4 if temp<75 else 0
        set_wheels(data,cmd,cmd)
        with viewer.lock():
            model.geom_rgba[gid]=[min(1,(temp-45)/35),.25,.2,1]
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
