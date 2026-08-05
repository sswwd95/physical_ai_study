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

checks=[
    ("입력 데이터 존재",DATA_FILE.exists()),
    ("설정 파일 존재",CONFIG_FILE.exists()),
    ("출력 폴더 존재",OUTPUT_DIR.exists()),
    ("로그 폴더 존재",LOG_DIR.exists()),
    ("모델 폴더 존재",MODEL_DIR.exists()),
    ("데이터 행 수 1 이상",len(pd.read_csv(DATA_FILE))>0),
    ("운영 로그 생성 가능",LOG_DIR.is_dir()),
]
check_df=pd.DataFrame(checks,columns=["check_item","passed"])
check_df["status"]=np.where(check_df["passed"],"OK","ACTION_REQUIRED")
print(check_df)
check_df.to_csv(OUTPUT_DIR/"ex379_operations_checklist.csv",index=False,encoding="utf-8-sig")
