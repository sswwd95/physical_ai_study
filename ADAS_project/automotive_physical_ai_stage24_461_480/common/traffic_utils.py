from pathlib import Path
import time, math, json
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
MODEL_PATH=ROOT/"models"/"traffic_v2x_viewer.xml"
OUTPUTS=ROOT/"outputs"
SIGNAL_PLAN=ROOT/"data"/"traffic_signal_plan.csv"

def load_project():
    import mujoco, mujoco.viewer
    model=mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data=mujoco.MjData(model)
    plan=pd.read_csv(SIGNAL_PLAN)
    return mujoco,model,data,plan

def set_ego(data,left,right):
    data.ctrl[0]=float(np.clip(left,-20,20))
    data.ctrl[1]=float(np.clip(right,-20,20))

def output_path(name):
    OUTPUTS.mkdir(parents=True,exist_ok=True)
    return OUTPUTS/name

def body_id(mujoco,model,name):
    return mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,name)

def pos_xy(data,bid):
    return float(data.xpos[bid][0]),float(data.xpos[bid][1])

def dist(a,b):
    return float(math.hypot(a[0]-b[0],a[1]-b[1]))

def signal_phase(t):
    cycle=14.0
    x=t%cycle
    if x<5:return "RED"
    if x<12:return "GREEN"
    return "YELLOW"

def set_signal(model,phase):
    colors={
      "RED":[1,.05,.05,1],
      "YELLOW":[1,.8,.05,1],
      "GREEN":[.05,1,.1,1]
    }
    names=["signal_red","signal_yellow","signal_green"]
    phases=["RED","YELLOW","GREEN"]
    for name,p in zip(names,phases):
        bid=model.body(name).id if hasattr(model,"body") else -1
    # color bodies through their geoms
    for geom_id in range(model.ngeom):
        body=model.geom_bodyid[geom_id]
        body_name=model.body(body).name if hasattr(model,"body") else ""
        if body_name in names:
            active=body_name==f"signal_{phase.lower()}"
            model.geom_rgba[geom_id]=colors[phase] if active else [.08,.08,.08,1]

def save_json(obj,name):
    p=output_path(name)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")
    return p
