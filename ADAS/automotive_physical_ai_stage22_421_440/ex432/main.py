import time
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
target=8.0; integral=0; prev=0
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        measured=float((data.qvel[-2]+data.qvel[-1])/2)
        error=target-measured
        integral=max(-5,min(5,integral+error*model.opt.timestep))
        derivative=(error-prev)/model.opt.timestep
        cmd=1.0*error+.3*integral+.02*derivative
        set_wheels(data,cmd,cmd)
        prev=error
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
