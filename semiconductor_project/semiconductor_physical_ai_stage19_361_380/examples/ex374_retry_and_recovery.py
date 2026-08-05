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

checkpoint=OUTPUT_DIR/"ex374_checkpoint.json"
max_retries=3
attempt=0
completed=False
while attempt<max_retries and not completed:
    attempt+=1
    try:
        ops_df=pd.read_csv(DATA_FILE)
        if len(ops_df)==0:
            raise ValueError("빈 데이터")
        completed=True
        checkpoint.write_text(json.dumps({"attempt":attempt,"status":"completed","rows":len(ops_df)},ensure_ascii=False,indent=2),encoding="utf-8")
    except Exception as e:
        checkpoint.write_text(json.dumps({"attempt":attempt,"status":"failed","error":str(e)},ensure_ascii=False,indent=2),encoding="utf-8")
if not completed:
    raise RuntimeError("최대 재시도 횟수 초과")
print(checkpoint.read_text(encoding="utf-8"))
