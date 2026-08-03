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
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
ops_df=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]
model=RandomForestClassifier(n_estimators=300,class_weight="balanced",random_state=42,n_jobs=-1)
model.fit(ops_df[features],ops_df["fault_flag"])
version=datetime.now().strftime("%Y%m%d_%H%M%S")
model_file=MODEL_DIR/f"fault_model_{version}.joblib"
meta_file=MODEL_DIR/f"fault_model_{version}.json"
joblib.dump(model,model_file)
meta={"version":version,"features":features,"rows":len(ops_df),"model_type":"RandomForestClassifier"}
meta_file.write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
print("모델:",model_file)
print("메타데이터:",meta_file)
