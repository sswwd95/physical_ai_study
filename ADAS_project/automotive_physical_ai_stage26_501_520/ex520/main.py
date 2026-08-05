import time,json,pandas as pd
from common.tb3_burger_utils import load_tb3,set_wheels,base_pose,output_path
mujoco,model,data,ids=load_tb3()
rows=[]; emergency_stops=0
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING
    viewer.cam.trackbodyid=ids["base_body"]
    viewer.cam.distance=2.0
    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT]=True
    while viewer.is_running() and data.time<20:
        pose=base_pose(data)
        virtual_obstacle_x=2.0
        distance=virtual_obstacle_x-pose["x_m"]
        if distance<.35:
            set_wheels(data,0,0); emergency_stops+=1
        elif data.time<6:set_wheels(data,4.5,4.5)
        elif data.time<10:set_wheels(data,-3.0,3.0)
        elif data.time<16:set_wheels(data,4.0,4.5)
        else:set_wheels(data,0,0)
        mujoco.mj_step(model,data)
        rows.append({"time_s":float(data.time),**pose,"virtual_distance_m":distance,
                     "left_ctrl":float(data.ctrl[0]),"right_ctrl":float(data.ctrl[1])})
        viewer.sync()
        time.sleep(model.opt.timestep)
csv_path=output_path("ex520_tb3_integrated_log.csv")
pd.DataFrame(rows).to_csv(csv_path,index=False,encoding="utf-8-sig")
report={"samples":len(rows),"emergency_stop_samples":emergency_stops,
        "final_pose":base_pose(data),"official_scene":str(model.names)}
json_path=output_path("ex520_tb3_integrated_report.json")
json_path.write_text(json.dumps(report,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
print(csv_path,json_path)
