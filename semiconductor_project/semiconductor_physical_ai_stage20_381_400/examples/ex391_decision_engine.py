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

file=OUTPUT_DIR/"ex390_integrated_inference.csv"
if not file.exists():
    raise FileNotFoundError("먼저 실습 390을 실행하세요.")
pred=pd.read_csv(file)
pred["action"]=np.select(
    [
        pred["fault_probability"]>=.90,
        pred["predicted_rul"]<=15,
        pred["fault_probability"]>=.70,
        pred["predicted_yield"]<93,
        pred["predicted_rul"]<=30
    ],
    ["EMERGENCY_INSPECTION","SCHEDULE_MAINTENANCE","SLOWDOWN_AND_CHECK","PROCESS_REVIEW","MONITOR_RUL"],
    default="CONTINUE")
print(pred["action"].value_counts())
pred.to_csv(OUTPUT_DIR/"ex391_decision_engine.csv",index=False,encoding="utf-8-sig")
