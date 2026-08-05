from pathlib import Path
import math
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"

WHEEL_RADIUS_M = 0.033
WHEEL_BASE_M = 0.160

def output_path(name: str) -> Path:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def wheels_to_twist(left_rad_s: float, right_rad_s: float,
                    wheel_radius: float = WHEEL_RADIUS_M,
                    wheel_base: float = WHEEL_BASE_M):
    linear = wheel_radius * (right_rad_s + left_rad_s) / 2.0
    angular = wheel_radius * (right_rad_s - left_rad_s) / wheel_base
    return linear, angular

def twist_to_wheels(linear_mps: float, angular_rps: float,
                    wheel_radius: float = WHEEL_RADIUS_M,
                    wheel_base: float = WHEEL_BASE_M):
    left = (linear_mps - angular_rps * wheel_base / 2.0) / wheel_radius
    right = (linear_mps + angular_rps * wheel_base / 2.0) / wheel_radius
    return left, right

def integrate_odometry(commands, dt=0.05, x0=0.0, y0=0.0, yaw0=0.0):
    x, y, yaw = x0, y0, yaw0
    rows = []
    time_s = 0.0
    for linear, angular, duration, mode in commands:
        steps = max(1, int(round(duration / dt)))
        for _ in range(steps):
            x += linear * math.cos(yaw) * dt
            y += linear * math.sin(yaw) * dt
            yaw += angular * dt
            yaw = math.atan2(math.sin(yaw), math.cos(yaw))
            time_s += dt
            rows.append([time_s, mode, linear, angular, x, y, yaw])
    return pd.DataFrame(rows, columns=[
        "time_s", "mode", "linear_mps", "angular_rps", "x_m", "y_m", "yaw_rad"
    ])

def path_length(df: pd.DataFrame) -> float:
    dx = df["x_m"].diff().fillna(0.0)
    dy = df["y_m"].diff().fillna(0.0)
    return float(np.sqrt(dx*dx + dy*dy).sum())
