# 검증 보고서

- Python 예제: 20개
- 라인별 해설 가이드: 20개
- Python 문법 검사: 전체 통과
- 분류 데이터: 900행 × 14열
- LOT 수: 30개
- 불량 라벨 수: 10건
- Logistic Regression, Decision Tree, Random Forest 포함
- 층화 분할과 LOT 그룹 분할 포함
- 클래스 가중치, 오버샘플링, 임계값 비교 포함
- ROC-AUC, PR-AUC, 교차검증 포함
- Excel 자동 분류 보고서 포함

## 권장 실행
```bat
conda env create -f environment.yml
conda activate semi-physical-ai-stage06
run_all_windows.bat
```

## 주의
불량 라벨은 교육용 합성 라벨입니다. 실제 반도체 프로젝트에서는 검사 장비 결과,
작업자 재판정, LOT 이력, 측정 불확실성을 함께 검토해야 합니다.
