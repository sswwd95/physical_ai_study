# 설계 기준

확률 모델:
- 전체 위험률: Beta-Bernoulli
- 특징별 위험도: Bayesian logistic regression
- 운전자·노면 차이: categorical effect와 hierarchical model
- 위험 판정: posterior probability와 비용 기반 threshold

비용 예:
- 미탐(FN): 10
- 오탐(FP): 2

실차에서는 위험도 모델을 제어기에 직접 연결하기 전에 독립 검증,
경고 히스테리시스, fail-safe, 차량·노면·운전자별 보정을 수행해야 합니다.
