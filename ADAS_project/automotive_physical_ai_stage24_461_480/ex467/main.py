import time
from common.traffic_utils import load_project,set_ego,body_id,pos_xy,dist
mujoco,model,data,plan=load_project()
ego=body_id(mujoco,model,"ego"); lead=body_id(mujoco,model,"lead_vehicle")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        data.mocap_pos[0]=[-2+.25*data.time,0,.12]
        gap=dist(pos_xy(data,ego),pos_xy(data,lead))
        cmd=4 if gap<1.5 else 7 if gap<3 else 9
        set_ego(data,cmd,cmd)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
