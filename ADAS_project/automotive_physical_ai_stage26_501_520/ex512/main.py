import time,pandas as pd
from common.tb3_burger_utils import load_tb3,set_wheels,base_pose,output_path
mujoco,model,data,ids=load_tb3()
rows=[]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<12:
        set_wheels(data,4.2,4.8)
        mujoco.mj_step(model,data)
        rows.append({"time_s":float(data.time),**base_pose(data),
                     "left_ctrl":float(data.ctrl[0]),"right_ctrl":float(data.ctrl[1])})
        viewer.sync()
        time.sleep(model.opt.timestep)
p=output_path("ex512_tb3_odometry.csv")
pd.DataFrame(rows).to_csv(p,index=False,encoding="utf-8-sig")
print(p)
