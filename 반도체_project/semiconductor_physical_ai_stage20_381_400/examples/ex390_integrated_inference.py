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

import joblib
registry_file=MODEL_DIR/"model_registry.json"
if not registry_file.exists():
    raise FileNotFoundError("먼저 실습 389를 실행하세요.")
registry=json.loads(registry_file.read_text(encoding="utf-8"))
data=pd.read_csv(DATA_FILE)
features=registry[0]["features"]
models={item["name"]:joblib.load(MODEL_DIR/item["file"]) for item in registry}
out=data[["timestamp","equipment_id","recipe","chamber_id"]].copy()
out["predicted_yield"]=models["yield"].predict(data[features])
out["fault_probability"]=models["fault"].predict_proba(data[features])[:,1]
out["predicted_rul"]=models["rul"].predict(data[features])
print(out.head().round(4))
out.to_csv(OUTPUT_DIR/"ex390_integrated_inference.csv",index=False,encoding="utf-8-sig")
