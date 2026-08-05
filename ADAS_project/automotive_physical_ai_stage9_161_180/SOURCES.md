# 설계 기준

PyMC의 Model, Normal, HalfNormal, StudentT, Deterministic, sample,
sample_posterior_predictive와 ArviZ summary·plot_posterior를 사용합니다.

바이어스는 부호가 가능하므로 Normal, 표준편차는 양수이므로 HalfNormal,
이상값 데이터는 Student-t, 여러 장치는 계층 모델로 구성합니다.
