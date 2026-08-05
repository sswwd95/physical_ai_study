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

scorecard_file=REPORT_DIR/"kpi_scorecard.csv"
scorecard=pd.read_csv(scorecard_file) if scorecard_file.exists() else pd.DataFrame()
text=f"""# 반도체 Physical AI 종합 프로젝트 사례

## 문제
공정 센서와 장비 상태 데이터를 이용해 수율 저하와 고장 위험을 조기에 파악한다.

## 접근
1. 데이터 계약과 품질 게이트
2. 공통 특징공학
3. 수율·고장·RUL 세 모델
4. 통합 의사결정 엔진
5. 안전 게이트
6. 운영 KPI와 보고서

## 결과
{scorecard.to_markdown(index=False) if not scorecard.empty else "실습 395 실행 후 KPI가 채워집니다."}

## 기여
- 종합 파이프라인 설계
- 모델 평가 자동화
- 운영 의사결정·안전 우선 로직
- 재현 가능한 산출물 구조
"""
file=PORTFOLIO_DIR/"portfolio_case_study.md"
file.write_text(text,encoding="utf-8")
print(file)
