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

decision_file=OUTPUT_DIR/"ex391_decision_engine.csv"
if not decision_file.exists():
    raise FileNotFoundError("먼저 실습 391을 실행하세요.")
pred=pd.read_csv(decision_file)
data=pd.read_csv(DATA_FILE)
pred["safety_gate"]=np.where(
    (data["temperature_c"]>80)|(data["pressure_pa"]>21)|(data["vibration_rms_g"]>.18),
    "FORCED_SAFE_STOP",
    "MODEL_DECISION")
pred["final_action"]=np.where(pred["safety_gate"]=="FORCED_SAFE_STOP","FORCED_SAFE_STOP",pred["action"])
print(pred["final_action"].value_counts())
