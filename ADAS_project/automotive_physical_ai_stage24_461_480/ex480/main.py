import time,json
from common.traffic_utils import *
mujoco,model,data,plan=load_project()
ego=body_id(mujoco,model,"ego"); lead=body_id(mujoco,model,"lead_vehicle")
cross=body_id(mujoco,model,"cross_vehicle"); ped=body_id(mujoco,model,"pedestrian")
rows=[]
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING
    viewer.cam.trackbodyid=ego
    viewer.cam.distance=4
    while viewer.is_running() and data.time<25:
        data.mocap_pos[0]=[-2+.25*data.time,0,.12]
        data.mocap_pos[1]=[0,-5+.25*data.time,.12]
        data.mocap_pos[3]=[0,-1.5+.12*data.time,.9]
        phase=signal_phase(data.time)
        lead_gap=dist(pos_xy(data,ego),pos_xy(data,lead))
        cross_gap=dist(pos_xy(data,ego),pos_xy(data,cross))
        ped_gap=dist(pos_xy(data,ego),pos_xy(data,ped))
        cmd=7
        reasons=[]
        if phase=="RED" and data.qpos[0]>-1.5:cmd=0; reasons.append("red_signal")
        if lead_gap<1.5:cmd=min(cmd,3); reasons.append("lead_gap")
        if cross_gap<2.0:cmd=0; reasons.append("cross_vehicle")
        if ped_gap<1.8:cmd=0; reasons.append("pedestrian")
        set_ego(data,cmd,cmd)
        rows.append({"time_s":float(data.time),"phase":phase,"command":cmd,
                     "lead_gap_m":lead_gap,"cross_gap_m":cross_gap,"ped_gap_m":ped_gap,
                     "reasons":reasons})
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
report={
 "samples":len(rows),
 "stop_samples":sum(r["command"]==0 for r in rows),
 "minimum_lead_gap_m":min(r["lead_gap_m"] for r in rows) if rows else None,
 "minimum_pedestrian_gap_m":min(r["ped_gap_m"] for r in rows) if rows else None}
p=save_json(report,"ex480_integrated_traffic_report.json")
print(report,p)
