# 예제 314 — 경로 횡방향 오차 P 제어

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage16_301_320
conda activate auto_physical_ai
python ex314\main.py
```

## 핵심 개념
- P: 현재 오차에 비례한 제어
- I: 누적 오차를 줄여 정상상태 오차 개선
- D: 오차 변화율을 이용해 급격한 변화를 완화
- 포화: 액추에이터가 낼 수 있는 최대 명령 제한
- 데드존: 작은 명령에는 액추에이터가 반응하지 않는 구간
- 안티와인드업: 포화 중 적분항이 과도하게 쌓이는 현상 방지

## ROS2 연결
- 목표 선속도·각속도: `/cmd_vel`
- 바퀴 속도: `/joint_states`
- 실제 선속도·각속도와 자세: `/odom`
- 제어기 상태와 포화 경고: `/diagnostics`

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import numpy as np, pandas as pd` | 제어 실습에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from common.control_utils import output_path` | 제어 실습에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `dt=.05; y=0.8; yaw=0.0; speed=.3; kp=1.4` | 목표값, 제어값, 상태값 또는 평가 지표를 계산합니다. |
| 4 | `rows=[]` | 목표값, 제어값, 상태값 또는 평가 지표를 계산합니다. |
| 5 | `for k in range(240):` | 현재 PID 제어 절차를 실행합니다. |
| 6 | `    yaw_rate=np.clip(-kp*y,-1.2,1.2)` | 목표값, 제어값, 상태값 또는 평가 지표를 계산합니다. |
| 7 | `    yaw += yaw_rate*dt` | 목표값, 제어값, 상태값 또는 평가 지표를 계산합니다. |
| 8 | `    y += speed*np.sin(yaw)*dt` | 목표값, 제어값, 상태값 또는 평가 지표를 계산합니다. |
| 9 | `    rows.append([k*dt,y,yaw,yaw_rate])` | 현재 PID 제어 절차를 실행합니다. |
| 10 | `df=pd.DataFrame(rows,columns=["time_s","lateral_error_m","yaw_rad","yaw_rate_cmd"])` | 목표값, 제어값, 상태값 또는 평가 지표를 계산합니다. |
| 11 | `p=output_path("ex314_lateral_error_control.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")` | 제어 로그·그래프·진단 결과를 저장합니다. |
| 12 | `print("final error:",df["lateral_error_m"].iloc[-1])` | 제어 성능과 저장 경로를 출력합니다. |

## 확인 문제
1. Ki를 지나치게 크게 설정하면 어떤 현상이 생기는가?
2. 출력 포화가 있을 때 안티와인드업이 필요한 이유는 무엇인가?
3. 제어 주기가 길어지면 미분항과 안정성에 어떤 영향이 생기는가?
