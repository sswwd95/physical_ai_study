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

required=[
    ROOT/"data",
    ROOT/"config",
    ROOT/"outputs",
    ROOT/"logs",
    ROOT/"models",
    DATA_FILE,
    CONFIG_FILE,
]
rows=[]
for path in required:
    rows.append({"path":str(path.relative_to(ROOT)),"exists":path.exists(),"type":"dir" if path.is_dir() else "file"})
result=pd.DataFrame(rows)
print(result)
if not result["exists"].all():
    raise FileNotFoundError("필수 운영 파일 또는 폴더가 없습니다.")
