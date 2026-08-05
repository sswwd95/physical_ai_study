import time,math,json
from common.project_viewer_utils import *
mujoco,model,data,path=load_project()
base=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"base")
obs=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"obstacle_1")
gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis")
rows=[]
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING
    viewer.cam.trackbodyid=base
    viewer.cam.distance=3.5
    while viewer.is_running() and data.time<25:
        x,y=float(data.qpos[0]),float(data.qpos[1])
        qw,qx,qy,qz=data.qpos[3:7]
        yaw=math.atan2(2*(qw*qz+qx*qy),1-2*(qy*qy+qz*qz))
        dist=body_distance(data,base,obs)
        left,right,idx,target,curv=pure_pursuit_command(path,x,y,yaw,.55,.8)
        error=abs(signed_cross_track_error(path,idx,x,y))
        risk=min(1.0,max(0.0,(1.6-dist)/1.6)+min(1.0,error))
        if dist<.8:left=right=0
        elif dist<1.6:left*=.4; right*=.4
        set_wheels(data,left,right)
        data.mocap_pos[0]=[path.iloc[target]["x_m"],path.iloc[target]["y_m"],.08]
        data.mocap_pos[1]=[x,y,.45]
        with viewer.lock():
            model.geom_rgba[gid]=[risk,1-risk,.1,1]
        mujoco.mj_step(model,data)
        rows.append({"time_s":float(data.time),"x_m":x,"y_m":y,
                     "distance_m":dist,"cross_track_error_m":error,
                     "risk":risk,"left_ctrl":float(data.ctrl[0]),"right_ctrl":float(data.ctrl[1])})
        viewer.sync(); time.sleep(model.opt.timestep)
report={
    "samples":len(rows),
    "minimum_distance_m":min(r["distance_m"] for r in rows) if rows else None,
    "maximum_cross_track_error_m":max(r["cross_track_error_m"] for r in rows) if rows else None,
    "maximum_risk":max(r["risk"] for r in rows) if rows else None}
p=save_json(report,"ex440_integrated_project_report.json")
print(report,p)
