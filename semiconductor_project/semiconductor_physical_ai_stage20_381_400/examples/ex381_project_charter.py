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

charter={
    "problem":"반도체 공정 수율 저하와 장비 고장 위험을 조기에 탐지",
    "objectives":[
        "수율 예측",
        "고장확률 예측",
        "RUL 예측",
        "운영 행동 추천",
        "안전 우선 의사결정"
    ],
    "scope":["데이터 검증","특징공학","모델링","평가","운영보고"],
    "out_of_scope":["실제 PLC 제어","실장비 자동정지"],
    "success_metrics":{
        "yield_mae_target":1.5,
        "fault_recall_target":0.80,
        "rul_mae_target":20.0
    }
}
file=PORTFOLIO_DIR/"project_charter.json"
file.write_text(json.dumps(charter,ensure_ascii=False,indent=2),encoding="utf-8")
print(file.read_text(encoding="utf-8"))
