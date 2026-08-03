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

ops_df=pd.read_csv(DATA_FILE)
checks=pd.DataFrame([
    {"check":"missing_values","failed":int(ops_df.isna().sum().sum())},
    {"check":"duplicate_rows","failed":int(ops_df.duplicated().sum())},
    {"check":"temperature_range","failed":int((~ops_df["temperature_c"].between(15,100)).sum())},
    {"check":"pressure_range","failed":int((~ops_df["pressure_pa"].between(0,50)).sum())},
    {"check":"yield_range","failed":int((~ops_df["yield_percent"].between(0,100)).sum())},
])
checks["passed"]=checks["failed"].eq(0)
print(checks)
checks.to_csv(OUTPUT_DIR/"ex366_data_quality_gate.csv",index=False,encoding="utf-8-sig")
if not checks["passed"].all():
    raise ValueError("데이터 품질 게이트 실패")
