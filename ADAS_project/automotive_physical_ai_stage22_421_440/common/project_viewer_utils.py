from pathlib import Path
import time
import math
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "automotive_project_viewer.xml"
PATH_CSV = ROOT / "data" / "project_path.csv"
OUTPUTS = ROOT / "outputs"

WHEEL_RADIUS = 0.06
WHEEL_BASE = 0.36

def output_path(name):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def load_project():
    import mujoco
    import mujoco.viewer
    model = mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data = mujoco.MjData(model)
    path = pd.read_csv(PATH_CSV)
    return mujoco, model, data, path

def set_wheels(data, left, right):
    data.ctrl[0] = float(np.clip(left, -20, 20))
    data.ctrl[1] = float(np.clip(right, -20, 20))

def wheels_to_twist(left, right):
    v = WHEEL_RADIUS * (right + left) / 2.0
    w = WHEEL_RADIUS * (right - left) / WHEEL_BASE
    return v, w

def nearest_path_index(path, x, y):
    dx = path["x_m"].to_numpy() - x
    dy = path["y_m"].to_numpy() - y
    return int(np.argmin(dx*dx + dy*dy))

def path_heading(path, idx):
    i0 = max(0, idx-1)
    i1 = min(len(path)-1, idx+1)
    dx = float(path.iloc[i1]["x_m"] - path.iloc[i0]["x_m"])
    dy = float(path.iloc[i1]["y_m"] - path.iloc[i0]["y_m"])
    return math.atan2(dy, dx)

def signed_cross_track_error(path, idx, x, y):
    px = float(path.iloc[idx]["x_m"])
    py = float(path.iloc[idx]["y_m"])
    h = path_heading(path, idx)
    return (x-px)*(-math.sin(h)) + (y-py)*math.cos(h)

def pure_pursuit_command(path, x, y, yaw, speed=0.5, lookahead=0.8):
    nearest = nearest_path_index(path, x, y)
    target = min(len(path)-1, nearest + 12)
    tx = float(path.iloc[target]["x_m"])
    ty = float(path.iloc[target]["y_m"])
    alpha = math.atan2(ty-y, tx-x) - yaw
    alpha = math.atan2(math.sin(alpha), math.cos(alpha))
    curvature = 2*math.sin(alpha)/max(lookahead, 1e-6)
    yaw_rate = speed*curvature
    left = (speed - yaw_rate*WHEEL_BASE/2)/WHEEL_RADIUS
    right = (speed + yaw_rate*WHEEL_BASE/2)/WHEEL_RADIUS
    return left, right, nearest, target, curvature

def realtime_loop(mujoco, model, data, viewer, duration, control=None, logger=None):
    start = time.time()
    while viewer.is_running() and time.time()-start < duration:
        tick = time.time()
        if control:
            control(model, data)
        mujoco.mj_step(model, data)
        if logger:
            logger(model, data)
        viewer.sync()
        delay = model.opt.timestep - (time.time()-tick)
        if delay > 0:
            time.sleep(delay)

def body_distance(data, id_a, id_b):
    return float(np.linalg.norm(data.xpos[id_a] - data.xpos[id_b]))

def save_json(data, name):
    p = output_path(name)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return p
