import time
from common.project_viewer_utils import load_project,set_wheels
mujoco,model,data,path=load_project()
next_print=0
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<12:
        set_wheels(data,6,7)
        mujoco.mj_step(model,data)
        if data.time>=next_print:
            print("time",round(data.time,2),"sensordata",data.sensordata.copy())
            next_print+=1
        viewer.sync()
        time.sleep(model.opt.timestep)
