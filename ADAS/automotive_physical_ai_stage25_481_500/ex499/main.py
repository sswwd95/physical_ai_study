import time,pandas as pd
from common.dynamics_utils import load_project,set_all,chassis_rpy,suspension_positions,output_path
mujoco,model,data,plan=load_project()
rows=[]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<15:
        set_all(data,10); mujoco.mj_step(model,data)
        roll,pitch,yaw=chassis_rpy(data); susp=suspension_positions(model,data)
        rows.append([data.time,*data.qpos[:3],roll,pitch,yaw,*susp.values()])
        viewer.sync(); time.sleep(model.opt.timestep)
p=output_path("ex499_dynamics_test_log.csv")
cols=["time_s","x_m","y_m","z_m","roll","pitch","yaw","fl","fr","rl","rr"]
pd.DataFrame(rows,columns=cols).to_csv(p,index=False)
print(p)
