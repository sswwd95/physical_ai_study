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
model=joblib.load(model_files[-1])
ops_df=pd.read_csv(DATA_FILE)
features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]
prob=model.predict_proba(ops_df[features])[:,1]
summary=pd.DataFrame([{
    "prediction_count":len(prob),
    "mean_probability":prob.mean(),
    "p95_probability":np.quantile(prob,.95),
    "above_070":int((prob>=.70).sum()),
    "above_090":int((prob>=.90).sum())
}])
print(summary.round(4))
summary.to_csv(OUTPUT_DIR/"ex371_prediction_monitoring.csv",index=False,encoding="utf-8-sig")
