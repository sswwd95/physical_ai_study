# 예제 500 — 차량 동역학 통합 시험 Viewer

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage25_481_500
conda activate automotive_dynamics_viewer
python ex500\main.py
```

## 신규 학습영역
이 예제는 기존 제어·교통·V2X·센서 고장주입과 달리 차량의 서스펜션, 롤·피치, 적재 편심, 타이어, 경사로, 연석, 견인 안정성과 전복 위험을 다룹니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,math,json` | 차량 동역학 Viewer용 모듈을 불러옵니다. |
| 2 | `from common.dynamics_utils import *` | 차량 동역학 Viewer용 모듈을 불러옵니다. |
| 3 | `mujoco,model,data,plan=load_project()` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 4 | `gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis_geom")` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 5 | `rows=[]` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 6 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 동역학 시험 루프와 함께 Viewer를 실행합니다. |
| 7 | `    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 8 | `    viewer.cam.trackbodyid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"chassis")` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 9 | `    viewer.cam.distance=5` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 10 | `    while viewer.is_running() and data.time<28:` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 11 | `        t=data.time` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 12 | `        if t<6:set_all(data,10)` | 4개 바퀴 구동 명령을 설정합니다. |
| 13 | `        elif t<10:set_all(data,0)` | 4개 바퀴 구동 명령을 설정합니다. |
| 14 | `        elif t<17:` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 15 | `            diff=5*math.sin(t*1.3); set_drive(data,10-diff,10+diff,10-diff,10+diff)` | 4개 바퀴 구동 명령을 설정합니다. |
| 16 | `        elif t<23:set_all(data,12)` | 4개 바퀴 구동 명령을 설정합니다. |
| 17 | `        else:set_all(data,6)` | 4개 바퀴 구동 명령을 설정합니다. |
| 18 | `        mujoco.mj_step(model,data)` | 차량 동역학 물리 상태를 한 스텝 진행합니다. |
| 19 | `        roll,pitch,yaw=chassis_rpy(data)` | 차체의 롤·피치·요 각도를 계산합니다. |
| 20 | `        susp=suspension_positions(model,data)` | 4개 서스펜션의 변위를 읽습니다. |
| 21 | `        risk=min(1,max(abs(roll)/.45,abs(pitch)/.35))` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 22 | `        with viewer.lock(): model.geom_rgba[gid]=[risk,1-risk,.1,1]` | 모델 물성이나 색상을 안전하게 변경합니다. |
| 23 | `        rows.append({"time_s":float(t),"roll_rad":roll,"pitch_rad":pitch,` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 24 | `                     "risk":risk,**susp})` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 25 | `        viewer.sync(); time.sleep(model.opt.timestep)` | 물리 상태와 Viewer 표시를 동기화합니다. |
| 26 | `report={` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 27 | ` "samples":len(rows),` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 28 | ` "max_abs_roll_rad":max(abs(r["roll_rad"]) for r in rows) if rows else None,` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 29 | ` "max_abs_pitch_rad":max(abs(r["pitch_rad"]) for r in rows) if rows else None,` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 30 | ` "max_risk":max(r["risk"] for r in rows) if rows else None}` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 31 | `p=save_json(report,"ex500_integrated_dynamics_report.json")` | 시험 결과를 CSV 또는 JSON으로 저장합니다. |
| 32 | `print(report,p)` | 롤·피치·서스펜션·시험 결과를 출력합니다. |

## 확인 문제
1. 서스펜션 강성과 감쇠가 승차감과 안정성에 어떤 영향을 주는가?
2. 적재물 위치가 롤·피치와 축하중에 어떤 영향을 주는가?
3. 트레일러 스웨이와 전복 위험을 줄이려면 어떤 제한이 필요한가?
