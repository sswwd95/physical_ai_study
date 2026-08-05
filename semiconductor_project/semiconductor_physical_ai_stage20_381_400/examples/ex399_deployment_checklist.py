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

items=[
    ("환경 재현","environment.yml 검증"),
    ("데이터 계약","컬럼·범위·결측 규칙 검증"),
    ("모델 버전","모델 파일·메타데이터 확인"),
    ("평가 기준","KPI 목표 통과 확인"),
    ("안전 게이트","모델보다 인터록 우선 확인"),
    ("모니터링","드리프트·성능·경보 확인"),
    ("복구","로그·체크포인트·재실행 절차 확인"),
    ("문서","README·운영가이드·포트폴리오 확인")
]
check=pd.DataFrame(items,columns=["area","check_item"])
check["status"]="TO_REVIEW"
print(check)
check.to_csv(PORTFOLIO_DIR/"deployment_checklist.csv",index=False,encoding="utf-8-sig")
