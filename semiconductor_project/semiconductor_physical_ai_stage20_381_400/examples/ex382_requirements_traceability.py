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

requirements=[
    {"id":"REQ-01","requirement":"수율 예측","implementation":"ex386","verification":"MAE/R2"},
    {"id":"REQ-02","requirement":"고장 확률","implementation":"ex387","verification":"Recall/F1"},
    {"id":"REQ-03","requirement":"RUL 예측","implementation":"ex388","verification":"MAE/R2"},
    {"id":"REQ-04","requirement":"통합 추론","implementation":"ex390","verification":"output schema"},
    {"id":"REQ-05","requirement":"안전 우선","implementation":"ex392","verification":"safety gate tests"},
    {"id":"REQ-06","requirement":"운영 보고서","implementation":"ex400","verification":"Excel sheets"}
]
df_req=pd.DataFrame(requirements)
print(df_req)
df_req.to_csv(REPORT_DIR/"requirements_traceability.csv",index=False,encoding="utf-8-sig")
