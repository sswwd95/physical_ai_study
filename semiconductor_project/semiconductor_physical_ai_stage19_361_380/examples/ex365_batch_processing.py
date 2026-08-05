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

with CONFIG_FILE.open("r",encoding="utf-8") as f:
    config=json.load(f)
batch_size=int(config["batch_size"])
ops_df=pd.read_csv(DATA_FILE)
rows=[]
for start in range(0,len(ops_df),batch_size):
    batch=ops_df.iloc[start:start+batch_size]
    rows.append({
        "batch_no":len(rows)+1,
        "start_row":start,
        "end_row":start+len(batch)-1,
        "row_count":len(batch),
        "mean_yield":batch["yield_percent"].mean(),
        "fault_count":int(batch["fault_flag"].sum())
    })
out=pd.DataFrame(rows)
print(out)
out.to_csv(OUTPUT_DIR/"ex365_batch_summary.csv",index=False,encoding="utf-8-sig")
