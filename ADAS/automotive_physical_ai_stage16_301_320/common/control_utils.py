from pathlib import Path
import math
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
MODEL_PATH = ROOT / "models" / "tb3_burger_training.xml"
WHEEL_RADIUS = 0.033
WHEEL_BASE = 0.160

def output_path(name):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

class PID:
    def __init__(self, kp, ki=0.0, kd=0.0, output_limit=None, integral_limit=None):
        self.kp = float(kp)
        self.ki = float(ki)
        self.kd = float(kd)
        self.output_limit = output_limit
        self.integral_limit = integral_limit
        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self):
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, target, measurement, dt):
        error = target - measurement
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        candidate_integral = self.integral + error * dt
        if self.integral_limit is not None:
            candidate_integral = float(np.clip(candidate_integral, -self.integral_limit, self.integral_limit))
        raw = self.kp*error + self.ki*candidate_integral + self.kd*derivative
        output = raw
        if self.output_limit is not None:
            output = float(np.clip(raw, -self.output_limit, self.output_limit))
        # Conditional integration anti-windup
        if self.output_limit is None or output == raw or np.sign(error) != np.sign(raw):
            self.integral = candidate_integral
        self.prev_error = error
        return output, error, self.integral, derivative

def wheels_to_twist(left, right):
    v = WHEEL_RADIUS * (right + left) / 2.0
    w = WHEEL_RADIUS * (right - left) / WHEEL_BASE
    return v, w

def twist_to_wheels(v, w):
    left = (v - w*WHEEL_BASE/2.0) / WHEEL_RADIUS
    right = (v + w*WHEEL_BASE/2.0) / WHEEL_RADIUS
    return left, right

def simulate_first_order(controller, target, duration=8.0, dt=0.02, tau=0.55,
                         deadzone=0.0, disturbance=None):
    y = 0.0
    rows = []
    steps = int(duration/dt)
    for k in range(steps):
        time_s = k*dt
        ref = target(time_s) if callable(target) else float(target)
        u, e, integ, deriv = controller.update(ref, y, dt)
        applied = 0.0 if abs(u) < deadzone else u
        d = disturbance(time_s) if disturbance else 0.0
        y += ((applied + d) - y) / tau * dt
        rows.append([time_s, ref, y, u, applied, e, integ, deriv])
    return pd.DataFrame(rows, columns=[
        "time_s","target","measurement","control","applied_control",
        "error","integral","derivative"
    ])

def error_metrics(df):
    e = df["error"].to_numpy()
    return {
        "mae": float(np.mean(np.abs(e))),
        "rmse": float(np.sqrt(np.mean(e**2))),
        "max_abs_error": float(np.max(np.abs(e))),
        "final_error": float(e[-1]),
    }
