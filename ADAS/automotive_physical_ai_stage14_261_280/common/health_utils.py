from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "vehicle_component_health.csv"
OUTPUTS = ROOT / "outputs"

FEATURES = [
    "motor_temp_c","motor_current_a","bearing_vibration_g",
    "battery_voltage_v","battery_internal_resistance_ohm",
    "wheel_friction_index"
]

def load_data():
    return pd.read_csv(DATA_PATH)

def output_path(name):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def moving_slope(series, window=100):
    x = np.arange(window)
    values = np.full(len(series), np.nan)
    arr = np.asarray(series)
    for i in range(window-1, len(arr)):
        y = arr[i-window+1:i+1]
        values[i] = np.polyfit(x, y, 1)[0]
    return values

def rmse(a,b):
    a=np.asarray(a); b=np.asarray(b)
    return float(np.sqrt(np.mean((a-b)**2)))

def save_json(data,name):
    p=output_path(name)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
    return p
