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

import joblib
model_files=sorted(MODEL_DIR.glob("fault_model_*.joblib"))
if not model_files:
    raise FileNotFoundError("먼저 실습 369를 실행하세요.")
latest=model_files[-1]
model=joblib.load(latest)
ops_df=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]
ops_df["predicted_fault"]=model.predict(ops_df[features])
ops_df["fault_probability"]=model.predict_proba(ops_df[features])[:,1]
print(ops_df[["predicted_fault","fault_probability"]].head())
