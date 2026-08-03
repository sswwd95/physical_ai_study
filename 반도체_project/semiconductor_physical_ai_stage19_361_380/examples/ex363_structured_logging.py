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

log_file=LOG_DIR/"stage19_operations.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.FileHandler(log_file,encoding="utf-8"),logging.StreamHandler()]
)
logging.info("운영 자동화 시작")
ops_df=pd.read_csv(DATA_FILE)
logging.info("데이터 로드 완료: %d행",len(ops_df))
logging.info("운영 자동화 정상 종료")
print("로그 파일:",log_file)
