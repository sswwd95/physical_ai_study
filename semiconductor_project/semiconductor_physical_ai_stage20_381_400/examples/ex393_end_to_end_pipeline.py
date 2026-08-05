from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "final_project_data.csv"
CONFIG_FILE = ROOT / "config" / "project_config.json"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"
PORTFOLIO_DIR = ROOT / "portfolio"

for directory in [OUTPUT_DIR, MODEL_DIR, REPORT_DIR, PORTFOLIO_DIR]:
    directory.mkdir(exist_ok=True)

def validate(df):
    required=["timestamp","equipment_id","yield_percent","fault_flag","rul_cycles"]
    missing=[c for c in required if c not in df.columns]
    if missing:
        raise ValueError(missing)
    return df

data=validate(pd.read_csv(DATA_FILE))
data["health_score"]=np.exp(
    -(.3*np.abs(data["temperature_c"]-72)+.25*np.abs(data["pressure_pa"]-18)+
      5*np.maximum(data["vibration_rms_g"]-.09,0)+.04*np.maximum(data["particle_count"]-8,0))
)
result=data[["timestamp","equipment_id","yield_percent","fault_flag","rul_cycles","health_score"]]
result.to_csv(OUTPUT_DIR/"ex393_end_to_end_result.csv",index=False,encoding="utf-8-sig")
print(result.head().round(4))
