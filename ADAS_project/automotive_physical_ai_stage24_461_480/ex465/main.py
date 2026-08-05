import time
from common.traffic_utils import load_project,set_ego,body_id,pos_xy,dist
mujoco,model,data,plan=load_project()
ego=body_id(mujoco,model,"ego"); cross=body_id(mujoco,model,"cross_vehicle")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<20:
        data.mocap_pos[1]=[0,-5+.5*data.time,.12]
        d=dist(pos_xy(data,ego),pos_xy(data,cross))
        set_ego(data,0,0) if d<2.0 else set_ego(data,7,7)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
