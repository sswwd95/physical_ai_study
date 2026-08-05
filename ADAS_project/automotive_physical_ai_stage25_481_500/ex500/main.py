import time,math,json
from common.dynamics_utils import *
mujoco,model,data,plan=load_project()
gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis_geom")
rows=[]
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING
    viewer.cam.trackbodyid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"chassis")
    viewer.cam.distance=5
    while viewer.is_running() and data.time<28:
        t=data.time
        if t<6:set_all(data,10)
        elif t<10:set_all(data,0)
        elif t<17:
            diff=5*math.sin(t*1.3); set_drive(data,10-diff,10+diff,10-diff,10+diff)
        elif t<23:set_all(data,12)
        else:set_all(data,6)
        mujoco.mj_step(model,data)
        roll,pitch,yaw=chassis_rpy(data)
        susp=suspension_positions(model,data)
        risk=min(1,max(abs(roll)/.45,abs(pitch)/.35))
        with viewer.lock(): model.geom_rgba[gid]=[risk,1-risk,.1,1]
        rows.append({"time_s":float(t),"roll_rad":roll,"pitch_rad":pitch,
                     "risk":risk,**susp})
        viewer.sync(); time.sleep(model.opt.timestep)
report={
 "samples":len(rows),
 "max_abs_roll_rad":max(abs(r["roll_rad"]) for r in rows) if rows else None,
 "max_abs_pitch_rad":max(abs(r["pitch_rad"]) for r in rows) if rows else None,
 "max_risk":max(r["risk"] for r in rows) if rows else None}
p=save_json(report,"ex500_integrated_dynamics_report.json")
print(report,p)
