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
split=int(len(ops_df)*.7)
train=ops_df.iloc[:split]
current=ops_df.iloc[split:]
features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]
rows=[]
for col in features:
    mean_diff=abs(current[col].mean()-train[col].mean())/(train[col].std()+1e-9)
    std_ratio=current[col].std()/(train[col].std()+1e-9)
    rows.append({"feature":col,"standardized_mean_diff":mean_diff,"std_ratio":std_ratio,"drift_alert":(mean_diff>.5)or(std_ratio<.7)or(std_ratio>1.3)})
out=pd.DataFrame(rows)
print(out.round(4))
out.to_csv(OUTPUT_DIR/"ex372_data_drift.csv",index=False,encoding="utf-8-sig")
