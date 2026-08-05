# 예제 479 — 교통 시나리오 이벤트 로그

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage24_461_480
conda activate automotive_traffic_viewer
python ex479\main.py
```

## 신규 학습영역
이 예제는 기존의 경로추종, 장애물 회피, 센서 고장주입, 주차·도킹과 달리 실제 도로의 신호, 보행자, 다중차량, V2X, 긴급차량, 공사구간, 기상·시야 및 운전자 인수전환을 다룹니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,pandas as pd` | 교통·V2X Viewer용 모듈을 불러옵니다. |
| 2 | `from common.traffic_utils import load_project,set_ego,signal_phase,output_path` | 교통·V2X Viewer용 모듈을 불러옵니다. |
| 3 | `mujoco,model,data,plan=load_project()` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 4 | `rows=[]` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 5 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 교통 시나리오 제어 루프와 함께 Viewer를 실행합니다. |
| 6 | `    while viewer.is_running() and data.time<18:` | 현재 교통환경 실습을 수행합니다. |
| 7 | `        phase=signal_phase(data.time)` | 현재 교통신호 단계를 계산합니다. |
| 8 | `        cmd=0 if phase=="RED" and data.qpos[0]>-1.5 else 7` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 9 | `        set_ego(data,cmd,cmd)` | 자차의 좌우 바퀴 명령을 적용합니다. |
| 10 | `        rows.append([data.time,phase,float(data.qpos[0]),cmd])` | 현재 교통환경 실습을 수행합니다. |
| 11 | `        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)` | 물리 시뮬레이션을 한 스텝 진행합니다. |
| 12 | `p=output_path("ex479_traffic_events.csv")` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 13 | `pd.DataFrame(rows,columns=["time_s","signal_phase","ego_x_m","command"]).to_csv(p,index=False)` | 현재 교통신호 단계를 계산합니다. |
| 14 | `print(p)` | 신호·거리·상태·결과를 출력합니다. |

## 확인 문제
1. 교통신호와 보행자 위험이 동시에 발생하면 어떤 우선순위가 필요한가?
2. V2X 정보가 지연되거나 틀릴 수 있다는 점을 어떻게 처리해야 하는가?
3. 자동운전에서 수동운전으로 전환할 때 어떤 상태를 기록해야 하는가?
