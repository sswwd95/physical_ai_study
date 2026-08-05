from pathlib import Path
import json, math
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
DATA_PATH=ROOT/"data"/"collision_risk_log.csv"
OUTPUTS=ROOT/"outputs"
MODEL_PATH=ROOT/"models"/"tb3_burger_training.xml"

def load_data():
    return pd.read_csv(DATA_PATH)

def output_path(name):
    OUTPUTS.mkdir(parents=True,exist_ok=True)
    return OUTPUTS/name

def braking_distance(speed, friction=0.7, gravity=9.81):
    return speed**2/(2*gravity*max(friction,1e-6))

def safe_distance(speed, reaction_time=1.2, friction=0.7, margin=2.0):
    return speed*reaction_time + braking_distance(speed,friction) + margin

def ttc(distance, relative_speed):
    if relative_speed <= 0:
        return float("inf")
    return distance/relative_speed

def risk_level(distance, safe_dist, ttc_s):
    if ttc_s < 1.0 or distance < 0.5*safe_dist:
        return "CRITICAL"
    if ttc_s < 2.0 or distance < 0.8*safe_dist:
        return "HIGH"
    if ttc_s < 4.0 or distance < safe_dist:
        return "CAUTION"
    return "NORMAL"

def hysteresis_alarm(values, on_threshold, off_threshold):
    state=False
    out=[]
    for value in values:
        if not state and value < on_threshold:
            state=True
        elif state and value > off_threshold:
            state=False
        out.append(state)
    return np.asarray(out,dtype=bool)

def confusion_counts(y_true,y_pred):
    y_true=np.asarray(y_true).astype(bool); y_pred=np.asarray(y_pred).astype(bool)
    return {
        "tp":int(np.sum(y_true & y_pred)),
        "fp":int(np.sum(~y_true & y_pred)),
        "tn":int(np.sum(~y_true & ~y_pred)),
        "fn":int(np.sum(y_true & ~y_pred)),
    }
