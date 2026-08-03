from pathlib import Path
import json
import logging
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "operations_stream.csv"
CONFIG_FILE = ROOT / "config" / "app_config.json"
OUTPUT_DIR = ROOT / "outputs"
LOG_DIR = ROOT / "logs"
MODEL_DIR = ROOT / "models"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

ops_df=pd.read_csv(DATA_FILE)
summary=ops_df.groupby("equipment_id").agg(
    mean_yield=("yield_percent","mean"),
    fault_rate=("fault_flag","mean"),
    mean_temperature=("temperature_c","mean"),
    mean_vibration=("vibration_rms_g","mean"),
    mean_cycle_time=("cycle_time_min","mean")
)
summary["health_grade"]=pd.cut(
    summary["fault_rate"],
    [-np.inf,.01,.03,.06,np.inf],
    labels=["A","B","C","D"]
)
print(summary.round(4))
summary.to_csv(OUTPUT_DIR/"ex376_equipment_health.csv",encoding="utf-8-sig")
