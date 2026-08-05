# 설계 기준

확률 모델:
- 고장확률: Beta-Bernoulli
- 수명분포: Weibull
- 부하·온도 영향: log-lifetime Bayesian regression
- 부품 간 편차: hierarchical model
- RUL: Bayesian linear regression and posterior predictive distribution

주의:
교육 예제는 고장 발생 데이터 중심의 단순 Weibull 모델입니다.
실무에서는 우측 검열을 우도에 직접 반영하는 생존분석 모델과 정비 이력을 사용해야 합니다.
