import time
from common.traffic_utils import load_project,set_ego,body_id,pos_xy,dist
mujoco,model,data,plan=load_project()
ego=body_id(mujoco,model,"ego"); ped=body_id(mujoco,model,"pedestrian")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<18:
        data.mocap_pos[3]=[0,-1.5+.2*data.time,.9]
        d=dist(pos_xy(data,ego),pos_xy(data,ped))
        set_ego(data,0,0) if d<1.8 else set_ego(data,6,6)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
