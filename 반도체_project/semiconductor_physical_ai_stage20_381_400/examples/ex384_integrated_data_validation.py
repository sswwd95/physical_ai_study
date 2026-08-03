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

data=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])
checks=pd.DataFrame([
    {"check":"missing","failed":int(data.isna().sum().sum())},
    {"check":"duplicates","failed":int(data.duplicated().sum())},
    {"check":"yield_range","failed":int((~data["yield_percent"].between(0,100)).sum())},
    {"check":"fault_values","failed":int((~data["fault_flag"].isin([0,1])).sum())},
    {"check":"rul_range","failed":int((~data["rul_cycles"].between(0,500)).sum())},
    {"check":"timestamp_order","failed":int((data["timestamp"].diff().dropna().dt.total_seconds()<0).sum())}
])
checks["passed"]=checks["failed"].eq(0)
print(checks)
checks.to_csv(OUTPUT_DIR/"ex384_data_validation.csv",index=False,encoding="utf-8-sig")
if not checks["passed"].all():
    raise ValueError("통합 데이터 품질 검증 실패")
