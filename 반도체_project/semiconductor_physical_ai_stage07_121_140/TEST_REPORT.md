# 검증 보고서

- Python 예제: 20개
- 라인별 해설 가이드: 20개
- Python 문법 검사: 전체 통과
- 다중 클래스 데이터: 1200행 × 13열
- 클래스 수: 4개
- 클래스 분포: {'normal': 1009, 'etch_rate': 77, 'particle': 64, 'uniformity': 50}
- Logistic Regression, One-vs-Rest, Decision Tree 포함
- Random Forest, HistGradientBoosting 포함
- GridSearchCV, RandomizedSearchCV 포함
- 클래스별 지표, 확률 보정, 오분류 분석 포함
- Excel 자동 다중 클래스 보고서 포함

## 권장 실행
```bat
conda env create -f environment.yml
conda activate semi-physical-ai-stage07
run_all_windows.bat
```

## 주의
본 데이터와 라벨은 교육용 합성 데이터입니다. 실제 프로젝트에서는 클래스 정의,
검사 판정 기준, 라벨 신뢰도, LOT 단위 데이터 누수를 함께 검토해야 합니다.
