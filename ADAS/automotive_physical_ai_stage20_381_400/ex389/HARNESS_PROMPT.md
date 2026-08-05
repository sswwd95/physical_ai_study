# 예제 389 소스 생성 하네스 프롬프트

## 역할
당신은 Stable-Baselines3와 자동차 강화학습을 담당한 20년차 Robotics·RL 엔지니어입니다.

## 목표
Windows 10, Anaconda, Gymnasium, Stable-Baselines3 환경에서 **Monitor 래퍼 적용** 실습을 작성합니다.

## 요구사항
1. `SimpleCarEnv`와 `common.sb3_utils`를 사용합니다.
2. PPO의 learning_rate, n_steps, batch_size, gamma, gae_lambda, clip_range를 설명합니다.
3. 학습·평가 환경을 분리합니다.
4. 모델 저장·로드·체크포인트·평가 콜백을 포함합니다.
5. deterministic 평가와 stochastic 평가를 구분합니다.
6. 안전 필터는 장애물 거리와 횡방향 오차를 확인합니다.
7. 결과 CSV·PNG·JSON과 모델은 outputs·models에 저장합니다.
8. ROS2 `/odom`, `/scan`, `/cmd_vel`, `/diagnostics` 연결점을 설명합니다.

## 검증 기준
- random seed를 고정합니다.
- 평가 에피소드 수와 학습 스텝을 코드에서 확인할 수 있어야 합니다.
- 안전 필터 적용 전후 충돌·차선이탈을 비교합니다.
