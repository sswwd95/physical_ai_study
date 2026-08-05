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

summary="""# 최종 발표 1페이지 요약

## 프로젝트
반도체 Physical AI 기반 수율·고장·RUL 통합 예측

## 핵심 문제
센서 이상과 공정 편차를 조기에 감지해 품질 손실과 정지 위험을 줄인다.

## 해결 구조
데이터 품질 → 특징공학 → 3개 모델 → 통합 의사결정 → 안전 게이트 → 운영 보고

## 주요 산출물
- 수율 예측
- 고장 확률
- RUL 예측
- 장비별 행동 추천
- 안전 우선 정책
- KPI·오차·운영 보고서

## 시연 순서
1. 데이터 검증
2. 모델 학습
3. 통합 추론
4. 의사결정
5. 보고서 확인
"""
file=PORTFOLIO_DIR/"presentation_one_page.md"
file.write_text(summary,encoding="utf-8")
print(file)
