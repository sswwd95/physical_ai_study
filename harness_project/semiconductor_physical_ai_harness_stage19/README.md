# 반도체 Physical AI 하네스 엔지니어링 — 19단계

실습 091~095는 Decision Tree·Random Forest 기반 불량 예측, 모델 비교, 확률 보정, Permutation Importance를 다룹니다.

## 포함 내용
- 시간 순서 기반 학습·테스트 분할
- Decision Tree와 Random Forest
- Logistic Regression 포함 모델 비교
- Average Precision 기반 순위
- Isotonic 확률 보정
- Brier score·Log loss
- Permutation Importance
- Lot별 보정 위험·고위험 Wafer 대시보드
- 합성 Wafer 공정 데이터
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_091_train_tree_models.py
python examples\example_092_compare_models.py
python examples\example_093_probability_calibration.py
python examples\example_094_permutation_importance.py
python examples\example_095_ensemble_dashboard.py

pytest -q
```

예측 결과는 교육용입니다. 실제 Wafer 폐기, 장비 정지, Recipe 변경에는 품질검증과 승인 절차가 필요합니다.
