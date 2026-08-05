import time,pandas as pd
from common.project_viewer_utils import load_project,set_wheels,output_path
mujoco,model,data,path=load_project()
rows=[]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<10:
        set_wheels(data,6,6)
        mujoco.mj_step(model,data)
        rows.append([data.time,*data.qpos[:3],*data.qvel[:3]])
        viewer.sync()
        time.sleep(model.opt.timestep)
out=output_path("ex424_odometry_log.csv")
pd.DataFrame(rows,columns=["time_s","x_m","y_m","z_m","vx","vy","vz"]).to_csv(out,index=False)
print(out)
