# 검증 보고서

- Python 예제: 20개
- 라인별 해설 가이드: 20개
- Python 문법 검사: 전체 통과
- 수율 회귀 데이터: 1000행 × 15열
- LOT 수: 100개
- 수율 평균: 92.401%
- 수율 최소: 86.849%
- 수율 최대: 96.700%
- Linear, Ridge, Lasso, Elastic Net 포함
- Decision Tree, Random Forest, Gradient Boosting 포함
- 잔차·저수율 구간·교차검증·GridSearchCV 포함
- 부트스트랩 예측구간과 Excel 자동 보고서 포함

## 권장 실행
```bat
conda env create -f environment.yml
conda activate semi-physical-ai-stage08
run_all_windows.bat
```

## 주의
수율은 교육용 합성 목표값입니다. 실제 프로젝트에서는 검사 공정, 샘플링 비율,
재측정 규칙, LOT 병합 기준과 데이터 누수를 함께 검토해야 합니다.
