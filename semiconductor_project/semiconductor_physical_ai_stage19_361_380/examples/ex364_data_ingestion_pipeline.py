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

def load_and_validate(path):
    df=pd.read_csv(path,parse_dates=["timestamp"])
    required=["timestamp","equipment_id","temperature_c","pressure_pa","yield_percent","fault_flag"]
    missing=[c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"필수 컬럼 누락: {missing}")
    if df.empty:
        raise ValueError("입력 데이터가 비어 있습니다.")
    return df.sort_values("timestamp").reset_index(drop=True)

ops_df=load_and_validate(DATA_FILE)
print(ops_df.head())
print("행 수:",len(ops_df))
