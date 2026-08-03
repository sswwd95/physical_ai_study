# 반도체 Physical AI 하네스 엔지니어링 — 20단계

실습 096~100은 불균형 데이터 처리와 001~100 통합 미니 프로젝트를 다룹니다.

## 포함 내용
- 정상·불량 클래스 불균형 진단
- Random Under Sampling
- Random Over Sampling
- 최근접 이웃 기반 SMOTE 유사 합성
- Random Forest 비용 민감 학습
- class_weight 설정 비교
- FN·FP 비용 기반 모델 선택
- Lot별 실제·예측 위험
- 고위험 Wafer HTML 대시보드
- 합성 불균형 Wafer 데이터
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_096_class_imbalance_diagnostics.py
python examples\example_097_under_over_sampling.py
python examples\example_098_simple_smote_like.py
python examples\example_099_cost_sensitive_comparison.py
python examples\example_100_integrated_mini_project.py

pytest -q
```

모든 모델과 경보 기준은 교육용입니다. 실제 Wafer 폐기, 장비 정지, Recipe 변경에는 품질검증과 승인 절차가 필요합니다.
