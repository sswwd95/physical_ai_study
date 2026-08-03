# 반도체 Physical AI 하네스 엔지니어링 — 18단계

실습 086~090은 로지스틱 회귀를 이용한 Wafer 불량 예측과 임계값 최적화를 다룹니다.

## 포함 내용
- 시간 순서 기반 학습·테스트 분할
- 숫자형·범주형 통합 전처리
- 불균형 클래스 로지스틱 회귀
- Precision·Recall·F1·ROC-AUC·Average Precision
- 비용 기반 임계값 선택
- 회귀 계수와 오즈비
- Lot별 위험·고위험 Wafer HTML 대시보드
- 합성 Wafer 공정 데이터
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_086_train_logistic_regression.py
python examples\example_087_evaluate_classifier.py
python examples\example_088_optimize_threshold.py
python examples\example_089_logistic_feature_effects.py
python examples\example_090_defect_prediction_dashboard.py

pytest -q
```

예측 결과는 교육용입니다. 실제 Wafer 폐기, 장비 정지, Recipe 변경에는 품질 검증과 승인 절차가 필요합니다.
