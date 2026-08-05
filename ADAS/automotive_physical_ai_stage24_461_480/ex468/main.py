import time
from common.traffic_utils import load_project,set_ego,body_id,pos_xy,dist
mujoco,model,data,plan=load_project()
ego=body_id(mujoco,model,"ego"); lead=body_id(mujoco,model,"lead_vehicle")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<22:
        lead_x=-2+.3*data.time
        data.mocap_pos[0]=[lead_x,.2*.2,.12]
        gap=dist(pos_xy(data,ego),pos_xy(data,lead))
        error=gap-2.0
        cmd=max(0,min(10,6+2*error))
        set_ego(data,cmd,cmd)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
