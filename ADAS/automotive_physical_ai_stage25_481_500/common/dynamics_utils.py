from pathlib import Path
import time, math, json
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
MODEL_PATH=ROOT/"models"/"vehicle_dynamics_viewer.xml"
PLAN_PATH=ROOT/"data"/"dynamics_test_plan.csv"
OUTPUTS=ROOT/"outputs"

def load_project():
    import mujoco, mujoco.viewer
    model=mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data=mujoco.MjData(model)
    plan=pd.read_csv(PLAN_PATH)
    return mujoco,model,data,plan

def set_drive(data,fl,fr,rl,rr):
    data.ctrl[:]=np.clip([fl,fr,rl,rr],-30,30)

def set_all(data,value):
    set_drive(data,value,value,value,value)

def output_path(name):
    OUTPUTS.mkdir(parents=True,exist_ok=True)
    return OUTPUTS/name

def quat_to_rpy(q):
    qw,qx,qy,qz=q
    roll=math.atan2(2*(qw*qx+qy*qz),1-2*(qx*qx+qy*qy))
    pitch=math.asin(max(-1,min(1,2*(qw*qy-qz*qx))))
    yaw=math.atan2(2*(qw*qz+qx*qy),1-2*(qy*qy+qz*qz))
    return roll,pitch,yaw

def chassis_rpy(data):
    return quat_to_rpy(data.qpos[3:7])

def suspension_positions(model,data):
    names=["fl_suspension","fr_suspension","rl_suspension","rr_suspension"]
    values={}
    for name in names:
        jid=model.joint(name).id
        values[name]=float(data.qpos[model.jnt_qposadr[jid]])
    return values

def save_json(obj,name):
    p=output_path(name)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")
    return p
