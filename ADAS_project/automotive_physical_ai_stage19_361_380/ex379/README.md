# 예제 379 — 에피소드 통계 시각화

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage19_361_380
conda activate auto_physical_ai
python ex379\main.py
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
| 1 | `import numpy as np,pandas as pd` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 2 | `import matplotlib` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 3 | `matplotlib.use("Agg")` | 현재 강화학습 환경 절차를 실행합니다. |
| 4 | `import matplotlib.pyplot as plt` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 5 | `from envs.simple_car_env import SimpleCarEnv` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 6 | `from common.rl_utils import output_path` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 7 | `returns=[]` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 8 | `for seed in range(20):` | 현재 강화학습 환경 절차를 실행합니다. |
| 9 | `    env=SimpleCarEnv(max_steps=80,seed=seed); obs,_=env.reset(seed=seed); total=0` | 교육용 자동차 강화학습 환경을 생성합니다. |
| 10 | `    for _ in range(80):` | 현재 강화학습 환경 절차를 실행합니다. |
| 11 | `        action=np.array([.45,np.clip(-1.2*obs[1]-.8*obs[2],-1,1)],dtype=np.float32)` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 12 | `        obs,r,term,trunc,_=env.step(action); total+=r` | 행동을 적용하고 다음 관측·보상·종료상태를 받습니다. |
| 13 | `        if term or trunc: break` | 현재 강화학습 환경 절차를 실행합니다. |
| 14 | `    returns.append(total); env.close()` | 현재 강화학습 환경 절차를 실행합니다. |
| 15 | `fig,ax=plt.subplots(figsize=(8,4)); ax.plot(returns,marker="o"); ax.grid(True); ax.set_xlabel("Episode"); ax.set_ylabel("Return")` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 16 | `p=output_path("ex379_episode_returns.png"); fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)` | 실험 결과를 outputs 폴더에 저장합니다. |
| 17 | `print(pd.Series(returns).describe()); print(p)` | 환경 상태, 보상 또는 검증 결과를 출력합니다. |

## 확인 문제
1. terminated와 truncated는 어떻게 다른가?
2. 보상에서 행동비용을 넣는 이유는 무엇인가?
3. 관측값 정규화가 학습 안정성에 도움이 되는 이유는 무엇인가?
