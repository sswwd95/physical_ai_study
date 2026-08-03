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

contract={
    "timestamp":{"dtype":"datetime","nullable":False},
    "equipment_id":{"dtype":"string","nullable":False},
    "recipe":{"dtype":"string","nullable":False},
    "temperature_c":{"dtype":"float","range":[0,120]},
    "pressure_pa":{"dtype":"float","range":[0,50]},
    "vibration_rms_g":{"dtype":"float","range":[0,1]},
    "yield_percent":{"dtype":"float","range":[0,100]},
    "fault_flag":{"dtype":"int","allowed":[0,1]},
    "rul_cycles":{"dtype":"float","range":[0,500]}
}
file=REPORT_DIR/"data_contract.json"
file.write_text(json.dumps(contract,ensure_ascii=False,indent=2),encoding="utf-8")
print(file.read_text(encoding="utf-8"))
