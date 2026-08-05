# 예제 400 — PPO 학습·평가·안전 적용 통합 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage20_381_400
conda activate auto_physical_ai
python ex400\main.py
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
| 1 | `import json` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 2 | `from stable_baselines3 import PPO` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 3 | `from envs.simple_car_env import SimpleCarEnv` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 4 | `from common.sb3_utils import evaluate_policy_manual,safety_filter,output_path,model_path` | Stable-Baselines3·Gymnasium·분석 모듈을 불러옵니다. |
| 5 | `env=SimpleCarEnv(max_steps=120)` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 6 | `model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64,` | PPO 정책과 학습 하이퍼파라미터를 설정합니다. |
| 7 | `          learning_rate=3e-4,gamma=.99,gae_lambda=.95,clip_range=.2)` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 8 | `model.learn(total_timesteps=1800)` | 지정한 timesteps 동안 PPO 정책을 학습합니다. |
| 9 | `model_file=model_path("ex400_final_ppo")` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 10 | `model.save(str(model_file))` | 학습 모델을 저장하거나 다시 불러옵니다. |
| 11 | `base=evaluate_policy_manual(model,env,episodes=10,deterministic=True)` | 여러 에피소드의 평균 보상과 종료 원인을 평가합니다. |
| 12 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 13 | `returns=[]; collisions=departures=0` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 14 | `for seed in range(10):` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 15 | `    obs,_=env.reset(seed=seed); total=0` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 16 | `    while True:` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 17 | `        action,_=model.predict(obs,deterministic=True)` | 현재 관측에서 정책 행동을 계산합니다. |
| 18 | `        action=safety_filter(action,obs[4],obs[1])` | 정책 행동을 안전 조건에 맞게 제한합니다. |
| 19 | `        obs,r,term,trunc,info=env.step(action); total+=r` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 20 | `        if term or trunc:` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 21 | `            collisions+=int(info.get("collision",False))` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 22 | `            departures+=int(info.get("lane_departure",False))` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 23 | `            break` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 24 | `    returns.append(total)` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 25 | `safe={` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 26 | `    "episodes":10,` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 27 | `    "mean_return":float(__import__("numpy").mean(returns)),` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 28 | `    "std_return":float(__import__("numpy").std(returns)),` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 29 | `    "collisions":collisions,` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 30 | `    "lane_departures":departures}` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 31 | `report={` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 32 | `    "training_timesteps":1800,` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 33 | `    "algorithm":"PPO",` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 34 | `    "policy":"MlpPolicy",` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 35 | `    "base_evaluation":base,` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 36 | `    "safety_filtered_evaluation":safe,` | 정책 행동을 안전 조건에 맞게 제한합니다. |
| 37 | `    "saved_model":str(model_file.with_suffix(".zip"))` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 38 | `}` | 현재 PPO 학습·평가 절차를 실행합니다. |
| 39 | `p=output_path("ex400_integrated_report.json")` | 모델, 환경, 행동, 보상 또는 통계값을 계산합니다. |
| 40 | `p.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")` | 학습·평가 결과를 저장합니다. |
| 41 | `print(report); print(p)` | 학습 상태, 평가 결과 또는 저장 경로를 출력합니다. |
| 42 | `env.close()` | 현재 PPO 학습·평가 절차를 실행합니다. |

## 확인 문제
1. PPO의 clip_range가 너무 크거나 작으면 어떤 문제가 생기는가?
2. 학습 환경과 평가 환경을 분리해야 하는 이유는 무엇인가?
3. 강화학습 정책과 별도의 안전 필터가 필요한 이유는 무엇인가?
