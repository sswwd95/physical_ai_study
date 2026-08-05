from pathlib import Path
import math
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
MODEL_PATH = ROOT / "models" / "tb3_burger_training.xml"

def output_path(name):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def load_path(name="path_sine.csv"):
    return pd.read_csv(ROOT / "data" / name)

def wrap_angle(angle):
    return math.atan2(math.sin(angle), math.cos(angle))

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
    heading = path_heading(path, idx)
    nx = -math.sin(heading)
    ny = math.cos(heading)
    return (x-px)*nx + (y-py)*ny

def lookahead_index(path, start_idx, lookahead_distance):
    px = path["x_m"].to_numpy()
    py = path["y_m"].to_numpy()
    distance = 0.0
    for i in range(start_idx, len(path)-1):
        distance += math.hypot(px[i+1]-px[i], py[i+1]-py[i])
        if distance >= lookahead_distance:
            return i+1
    return len(path)-1

def pure_pursuit_control(path, x, y, yaw, speed, lookahead=0.8, wheelbase=0.16):
    nearest = nearest_path_index(path, x, y)
    target_idx = lookahead_index(path, nearest, lookahead)
    tx = float(path.iloc[target_idx]["x_m"])
    ty = float(path.iloc[target_idx]["y_m"])
    alpha = wrap_angle(math.atan2(ty-y, tx-x) - yaw)
    curvature = 2.0 * math.sin(alpha) / max(lookahead, 1e-6)
    yaw_rate = speed * curvature
    steering = math.atan(wheelbase * curvature)
    return yaw_rate, steering, nearest, target_idx, alpha, curvature

def stanley_control(path, x, y, yaw, speed, gain=1.2, softening=0.1):
    idx = nearest_path_index(path, x, y)
    heading = path_heading(path, idx)
    heading_error = wrap_angle(heading-yaw)
    cte = signed_cross_track_error(path, idx, x, y)
    correction = math.atan2(gain*cte, abs(speed)+softening)
    steering = wrap_angle(heading_error + correction)
    yaw_rate = speed * math.tan(steering) / 0.16
    return yaw_rate, steering, idx, cte, heading_error, correction

def simulate_tracker(path, controller, speed=0.6, duration=25.0, dt=0.05,
                     x0=0.0, y0=-0.8, yaw0=0.0, max_yaw_rate=1.5):
    x, y, yaw = x0, y0, yaw0
    rows = []
    for k in range(int(duration/dt)):
        result = controller(path, x, y, yaw, speed)
        yaw_rate = float(np.clip(result[0], -max_yaw_rate, max_yaw_rate))
        x += speed*math.cos(yaw)*dt
        y += speed*math.sin(yaw)*dt
        yaw = wrap_angle(yaw + yaw_rate*dt)
        idx = nearest_path_index(path, x, y)
        cte = signed_cross_track_error(path, idx, x, y)
        rows.append([k*dt, x, y, yaw, speed, yaw_rate, idx, cte])
    return pd.DataFrame(rows, columns=[
        "time_s","x_m","y_m","yaw_rad","speed_mps","yaw_rate_rps",
        "nearest_index","cross_track_error_m"
    ])

def tracking_metrics(df):
    e = df["cross_track_error_m"].to_numpy()
    return {
        "mae_cte_m": float(np.mean(np.abs(e))),
        "rmse_cte_m": float(np.sqrt(np.mean(e**2))),
        "max_abs_cte_m": float(np.max(np.abs(e))),
        "final_abs_cte_m": float(abs(e[-1])),
    }
