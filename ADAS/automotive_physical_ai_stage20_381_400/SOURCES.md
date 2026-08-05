# 설계 기준

PPO 기본값:
- learning_rate = 3e-4
- n_steps = 128 또는 256
- batch_size = 64
- gamma = 0.99
- gae_lambda = 0.95
- clip_range = 0.2

평가:
- 평균 에피소드 보상
- 평균 에피소드 길이
- 충돌 횟수
- 차선이탈 횟수
- deterministic·stochastic 정책 비교

실차 적용 전 안전 필터, 동작 제한, watchdog, 긴급정지,
도메인 랜덤화, Sim-to-Real 검증이 필요합니다.
