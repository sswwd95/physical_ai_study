import time,pandas as pd
from common.project_viewer_utils import *
mujoco,model,data,path=load_project()
base=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"base")
obs=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"obstacle_1")
rows=[]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        dist=body_distance(data,base,obs)
        set_wheels(data,7,7 if dist>1 else 0)
        mujoco.mj_step(model,data)
        rows.append([data.time,*data.qpos[:2],dist,*data.ctrl[:2]])
        viewer.sync(); time.sleep(model.opt.timestep)
out=output_path("ex439_project_diagnostics.csv")
pd.DataFrame(rows,columns=["time_s","x_m","y_m","obstacle_distance_m","left_ctrl","right_ctrl"]).to_csv(out,index=False)
print(out)
