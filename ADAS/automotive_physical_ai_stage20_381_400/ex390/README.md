# 예제 390 — EvalCallback 적용

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage20_381_400
conda activate auto_physical_ai
python ex390\main.py
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
| 1 | `from stable_baselines3 import PPO` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 2 | `from stable_baselines3.common.callbacks import EvalCallback` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 3 | `from envs.simple_car_env import SimpleCarEnv` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 4 | `from common.sb3_utils import output_path,model_path` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 5 | `train_env=SimpleCarEnv(max_steps=100)` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 6 | `eval_env=SimpleCarEnv(max_steps=100,seed=99)` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 7 | `callback=EvalCallback(eval_env,best_model_save_path=str(model_path("ex390_best")),` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 8 | `                      log_path=str(output_path("ex390_eval")),eval_freq=250,` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 9 | `                      n_eval_episodes=3,deterministic=True)` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 10 | `model=PPO("MlpPolicy",train_env,verbose=0,seed=42,n_steps=128,batch_size=64)` | PPO 정책과 학습 하이퍼파라미터를 설정합니다. |
| 11 | `model.learn(total_timesteps=1000,callback=callback)` | 지정한 timesteps 동안 PPO 정책을 학습합니다. |
| 12 | `print("evaluation callback complete")` | 학습 상태, 평가 결과 또는 저장 경로를 출력합니다. |
| 13 | `train_env.close(); eval_env.close()` | 현재 PPO 학습·평가 절차를 실행합니다. |

## 확인 문제
1. PPO의 clip_range가 너무 크거나 작으면 어떤 문제가 생기는가?
2. 학습 환경과 평가 환경을 분리해야 하는 이유는 무엇인가?
3. 강화학습 정책과 별도의 안전 필터가 필요한 이유는 무엇인가?
