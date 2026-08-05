import time,pandas as pd
from common.traffic_utils import load_project,set_ego,signal_phase,output_path
mujoco,model,data,plan=load_project()
rows=[]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        phase=signal_phase(data.time)
        cmd=0 if phase=="RED" and data.qpos[0]>-1.5 else 7
        set_ego(data,cmd,cmd)
        rows.append([data.time,phase,float(data.qpos[0]),cmd])
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
p=output_path("ex479_traffic_events.csv")
pd.DataFrame(rows,columns=["time_s","signal_phase","ego_x_m","command"]).to_csv(p,index=False)
print(p)
