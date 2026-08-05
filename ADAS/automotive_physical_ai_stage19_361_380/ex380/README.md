# 예제 380 — 강화학습 환경 통합 검증 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage19_361_380
conda activate auto_physical_ai
python ex380\main.py
```

## 핵심 개념
- 관측공간: 에이전트가 현재 상태를 파악하는 입력
- 행동공간: 에이전트가 선택할 수 있는 가속·조향 명령
- 보상: 바람직한 행동을 수치로 표현한 학습 신호
- terminated: 충돌·차선이탈처럼 환경 상태로 끝남
- truncated: 최대 스텝처럼 외부 제한으로 끝남
- 안전 필터: 학습 행동을 실제 적용 전 안전 범위로 제한

## ROS2 연결
- 관측 입력: `/odom`, `/imu`, `/scan`
- 행동 출력: `/cmd_vel`
- 종료·안전 상태: `/diagnostics`
- 실제 적용 전에는 시뮬레이터와 실차의 단위·주기·지연을 일치시켜야 합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import json,numpy as np` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 2 | `from gymnasium.utils.env_checker import check_env` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 3 | `from envs.simple_car_env import SimpleCarEnv` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 4 | `from common.rl_utils import output_path` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 5 | `env=SimpleCarEnv(max_steps=100,seed=42)` | 교육용 자동차 강화학습 환경을 생성합니다. |
| 6 | `check_env(env,skip_render_check=True)` | Gymnasium API 규격 준수 여부를 검사합니다. |
| 7 | `returns=[]; lengths=[]; terminations={"collision":0,"lane_departure":0,"truncated":0}` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 8 | `for seed in range(15):` | 현재 강화학습 환경 절차를 실행합니다. |
| 9 | `    obs,_=env.reset(seed=seed); total=0` | 환경을 초기화하고 최초 관측값을 받습니다. |
| 10 | `    for _ in range(100):` | 현재 강화학습 환경 절차를 실행합니다. |
| 11 | `        steering=np.clip(-1.2*obs[1]-.8*obs[2],-1,1)` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 12 | `        throttle=.45 if obs[4]>3 else -.6` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 13 | `        obs,r,term,trunc,info=env.step(np.array([throttle,steering],dtype=np.float32))` | 행동을 적용하고 다음 관측·보상·종료상태를 받습니다. |
| 14 | `        total+=r` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 15 | `        if term or trunc:` | 현재 강화학습 환경 절차를 실행합니다. |
| 16 | `            terminations["collision"]+=int(info.get("collision",False))` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 17 | `            terminations["lane_departure"]+=int(info.get("lane_departure",False))` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 18 | `            terminations["truncated"]+=int(trunc)` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 19 | `            break` | 현재 강화학습 환경 절차를 실행합니다. |
| 20 | `    returns.append(total); lengths.append(env.steps)` | 현재 강화학습 환경 절차를 실행합니다. |
| 21 | `report={` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 22 | `    "episodes":len(returns),` | 현재 강화학습 환경 절차를 실행합니다. |
| 23 | `    "mean_return":float(np.mean(returns)),` | 현재 강화학습 환경 절차를 실행합니다. |
| 24 | `    "std_return":float(np.std(returns)),` | 현재 강화학습 환경 절차를 실행합니다. |
| 25 | `    "mean_length":float(np.mean(lengths)),` | 현재 강화학습 환경 절차를 실행합니다. |
| 26 | `    "terminations":terminations,` | 현재 강화학습 환경 절차를 실행합니다. |
| 27 | `    "observation_shape":list(env.observation_space.shape),` | 행동 또는 관측 공간의 범위와 형태를 확인합니다. |
| 28 | `    "action_shape":list(env.action_space.shape),` | 행동 또는 관측 공간의 범위와 형태를 확인합니다. |
| 29 | `}` | 현재 강화학습 환경 절차를 실행합니다. |
| 30 | `p=output_path("ex380_integrated_rl_env_report.json")` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 31 | `p.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")` | 실험 결과를 outputs 폴더에 저장합니다. |
| 32 | `print(report); print(p)` | 환경 상태, 보상 또는 검증 결과를 출력합니다. |
| 33 | `env.close()` | 현재 강화학습 환경 절차를 실행합니다. |

## 확인 문제
1. terminated와 truncated는 어떻게 다른가?
2. 보상에서 행동비용을 넣는 이유는 무엇인가?
3. 관측값 정규화가 학습 안정성에 도움이 되는 이유는 무엇인가?
