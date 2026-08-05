# 예제 480 — 교통·V2X·다중차량 통합 Viewer

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage24_461_480
conda activate automotive_traffic_viewer
python ex480\main.py
```

## 신규 학습영역
이 예제는 기존의 경로추종, 장애물 회피, 센서 고장주입, 주차·도킹과 달리 실제 도로의 신호, 보행자, 다중차량, V2X, 긴급차량, 공사구간, 기상·시야 및 운전자 인수전환을 다룹니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,json` | 교통·V2X Viewer용 모듈을 불러옵니다. |
| 2 | `from common.traffic_utils import *` | 교통·V2X Viewer용 모듈을 불러옵니다. |
| 3 | `mujoco,model,data,plan=load_project()` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 4 | `ego=body_id(mujoco,model,"ego"); lead=body_id(mujoco,model,"lead_vehicle")` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 5 | `cross=body_id(mujoco,model,"cross_vehicle"); ped=body_id(mujoco,model,"pedestrian")` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 6 | `rows=[]` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 7 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 교통 시나리오 제어 루프와 함께 Viewer를 실행합니다. |
| 8 | `    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 9 | `    viewer.cam.trackbodyid=ego` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 10 | `    viewer.cam.distance=4` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 11 | `    while viewer.is_running() and data.time<25:` | 현재 교통환경 실습을 수행합니다. |
| 12 | `        data.mocap_pos[0]=[-2+.25*data.time,0,.12]` | 교통 참가자의 위치를 시간에 따라 이동시킵니다. |
| 13 | `        data.mocap_pos[1]=[0,-5+.25*data.time,.12]` | 교통 참가자의 위치를 시간에 따라 이동시킵니다. |
| 14 | `        data.mocap_pos[3]=[0,-1.5+.12*data.time,.9]` | 교통 참가자의 위치를 시간에 따라 이동시킵니다. |
| 15 | `        phase=signal_phase(data.time)` | 현재 교통신호 단계를 계산합니다. |
| 16 | `        lead_gap=dist(pos_xy(data,ego),pos_xy(data,lead))` | 교통 참가자 사이의 거리를 계산합니다. |
| 17 | `        cross_gap=dist(pos_xy(data,ego),pos_xy(data,cross))` | 교통 참가자 사이의 거리를 계산합니다. |
| 18 | `        ped_gap=dist(pos_xy(data,ego),pos_xy(data,ped))` | 교통 참가자 사이의 거리를 계산합니다. |
| 19 | `        cmd=7` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 20 | `        reasons=[]` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 21 | `        if phase=="RED" and data.qpos[0]>-1.5:cmd=0; reasons.append("red_signal")` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 22 | `        if lead_gap<1.5:cmd=min(cmd,3); reasons.append("lead_gap")` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 23 | `        if cross_gap<2.0:cmd=0; reasons.append("cross_vehicle")` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 24 | `        if ped_gap<1.8:cmd=0; reasons.append("pedestrian")` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 25 | `        set_ego(data,cmd,cmd)` | 자차의 좌우 바퀴 명령을 적용합니다. |
| 26 | `        rows.append({"time_s":float(data.time),"phase":phase,"command":cmd,` | 현재 교통환경 실습을 수행합니다. |
| 27 | `                     "lead_gap_m":lead_gap,"cross_gap_m":cross_gap,"ped_gap_m":ped_gap,` | 현재 교통환경 실습을 수행합니다. |
| 28 | `                     "reasons":reasons})` | 현재 교통환경 실습을 수행합니다. |
| 29 | `        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)` | 물리 시뮬레이션을 한 스텝 진행합니다. |
| 30 | `report={` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 31 | ` "samples":len(rows),` | 현재 교통환경 실습을 수행합니다. |
| 32 | ` "stop_samples":sum(r["command"]==0 for r in rows),` | 신호, 거리, 명령 또는 이벤트 값을 계산합니다. |
| 33 | ` "minimum_lead_gap_m":min(r["lead_gap_m"] for r in rows) if rows else None,` | 현재 교통환경 실습을 수행합니다. |
| 34 | ` "minimum_pedestrian_gap_m":min(r["ped_gap_m"] for r in rows) if rows else None}` | 현재 교통환경 실습을 수행합니다. |
| 35 | `p=save_json(report,"ex480_integrated_traffic_report.json")` | 교통 시나리오 결과를 저장합니다. |
| 36 | `print(report,p)` | 신호·거리·상태·결과를 출력합니다. |

## 확인 문제
1. 교통신호와 보행자 위험이 동시에 발생하면 어떤 우선순위가 필요한가?
2. V2X 정보가 지연되거나 틀릴 수 있다는 점을 어떻게 처리해야 하는가?
3. 자동운전에서 수동운전으로 전환할 때 어떤 상태를 기록해야 하는가?
