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
required_keys=["project_name","input_file","output_dir","log_level","yield_warning_threshold","batch_size"]
missing=[k for k in required_keys if k not in config]
if missing:
    raise KeyError(f"누락 설정: {missing}")
if config["batch_size"]<=0:
    raise ValueError("batch_size는 1 이상이어야 합니다.")
print(json.dumps(config,ensure_ascii=False,indent=2))
