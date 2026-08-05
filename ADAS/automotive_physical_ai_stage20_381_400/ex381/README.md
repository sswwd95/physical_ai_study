# 예제 381 — Stable-Baselines3 설치 확인

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage20_381_400
conda activate auto_physical_ai
python ex381\main.py
```

## 핵심 개념
- PPO: 정책 업데이트 폭을 제한해 학습 안정성을 높이는 정책경사 알고리즘
- deterministic 평가: 같은 관측에서 대표 행동을 사용
- stochastic 평가: 정책 확률분포에서 행동을 샘플링
- EvalCallback: 일정 주기마다 평가하고 최고 모델 저장
- CheckpointCallback: 학습 중간 모델 저장
- 안전 필터: 정책 행동을 실차 적용 전 제한하는 별도 계층

## ROS2 연결
- 관측: `/odom`, `/imu`, `/scan`
- 정책 행동: `/cmd_vel`
- 안전 필터: 속도·조향 명령 포화와 긴급 감속
- 진단: `/diagnostics`
- 학습 정책은 시뮬레이터에서 검증 후 단계적으로 실차에 적용해야 합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `try:` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 2 | `    import stable_baselines3 as sb3` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 3 | `except ImportError:` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 4 | `    print("Install stable-baselines3 using environment.yml")` | 학습 상태, 평가 결과 또는 저장 경로를 출력합니다. |
| 5 | `else:` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 6 | `    print("Stable-Baselines3:",sb3.__version__)` | 학습 상태, 평가 결과 또는 저장 경로를 출력합니다. |

## 확인 문제
1. PPO의 clip_range가 너무 크거나 작으면 어떤 문제가 생기는가?
2. 학습 환경과 평가 환경을 분리해야 하는 이유는 무엇인가?
3. 강화학습 정책과 별도의 안전 필터가 필요한 이유는 무엇인가?
