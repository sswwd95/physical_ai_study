# 예제 372 — 랜덤 정책 실행

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage19_361_380
conda activate auto_physical_ai
python ex372\main.py
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
| 1 | `import numpy as np` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 2 | `from envs.simple_car_env import SimpleCarEnv` | Gymnasium 환경과 분석에 필요한 모듈을 불러옵니다. |
| 3 | `env=SimpleCarEnv(max_steps=50,seed=7)` | 교육용 자동차 강화학습 환경을 생성합니다. |
| 4 | `obs,_=env.reset(seed=7)` | 환경을 초기화하고 최초 관측값을 받습니다. |
| 5 | `total=0` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 6 | `for _ in range(50):` | 현재 강화학습 환경 절차를 실행합니다. |
| 7 | `    action=env.action_space.sample()` | 행동 또는 관측 공간의 범위와 형태를 확인합니다. |
| 8 | `    obs,reward,terminated,truncated,info=env.step(action)` | 행동을 적용하고 다음 관측·보상·종료상태를 받습니다. |
| 9 | `    total+=reward` | 상태, 행동, 보상 또는 통계값을 계산합니다. |
| 10 | `    if terminated or truncated:` | 현재 강화학습 환경 절차를 실행합니다. |
| 11 | `        break` | 현재 강화학습 환경 절차를 실행합니다. |
| 12 | `print("steps:",env.steps,"return:",total,"final:",obs)` | 환경 상태, 보상 또는 검증 결과를 출력합니다. |
| 13 | `env.close()` | 현재 강화학습 환경 절차를 실행합니다. |

## 확인 문제
1. terminated와 truncated는 어떻게 다른가?
2. 보상에서 행동비용을 넣는 이유는 무엇인가?
3. 관측값 정규화가 학습 안정성에 도움이 되는 이유는 무엇인가?
