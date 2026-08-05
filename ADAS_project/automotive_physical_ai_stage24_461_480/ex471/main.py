import time
from common.traffic_utils import load_project,set_ego,body_id,pos_xy,dist
mujoco,model,data,plan=load_project()
ego=body_id(mujoco,model,"ego"); emg=body_id(mujoco,model,"emergency_vehicle")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        data.mocap_pos[2]=[-8+.45*data.time,-2+.1*data.time,.12]
        d=dist(pos_xy(data,ego),pos_xy(data,emg))
        set_ego(data,2,5) if d<3 else set_ego(data,7,7)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
