# 예제 440 — 자동차 Physical AI 프로젝트 통합 Viewer

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage22_421_440
conda activate automotive_project_viewer
python ex440\main.py
```

## 프로젝트 연결
이 예제는 자동차 Physical AI 과정에서 다룬 센서 분석, 오도메트리, 휠 슬립, 경로 추종, 안전거리, 이상 탐지, 예지보전 또는 강화학습 결과를 MuJoCo Viewer로 확인합니다.

## 실행 조건
- Windows GUI·OpenGL 환경
- MuJoCo 3.6.0
- Viewer 창을 닫으면 실행 루프가 종료됩니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,math,json` | 프로젝트 Viewer에 필요한 모듈과 공통 함수를 불러옵니다. |
| 2 | `from common.project_viewer_utils import *` | 프로젝트 Viewer에 필요한 모듈과 공통 함수를 불러옵니다. |
| 3 | `mujoco,model,data,path=load_project()` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 4 | `base=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"base")` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 5 | `obs=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"obstacle_1")` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 6 | `gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis")` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 7 | `rows=[]` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 8 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | Python 제어 루프와 함께 실행되는 passive Viewer를 엽니다. |
| 9 | `    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 10 | `    viewer.cam.trackbodyid=base` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 11 | `    viewer.cam.distance=3.5` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 12 | `    while viewer.is_running() and data.time<25:` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 13 | `        x,y=float(data.qpos[0]),float(data.qpos[1])` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 14 | `        qw,qx,qy,qz=data.qpos[3:7]` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 15 | `        yaw=math.atan2(2*(qw*qz+qx*qy),1-2*(qy*qy+qz*qz))` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 16 | `        dist=body_distance(data,base,obs)` | 차량과 장애물 사이의 3차원 거리를 계산합니다. |
| 17 | `        left,right,idx,target,curv=pure_pursuit_command(path,x,y,yaw,.55,.8)` | 현재 위치에서 경로 추종 바퀴 명령을 계산합니다. |
| 18 | `        error=abs(signed_cross_track_error(path,idx,x,y))` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 19 | `        risk=min(1.0,max(0.0,(1.6-dist)/1.6)+min(1.0,error))` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 20 | `        if dist<.8:left=right=0` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 21 | `        elif dist<1.6:left*=.4; right*=.4` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 22 | `        set_wheels(data,left,right)` | 좌우 바퀴 속도 명령을 안전 범위로 제한해 적용합니다. |
| 23 | `        data.mocap_pos[0]=[path.iloc[target]["x_m"],path.iloc[target]["y_m"],.08]` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 24 | `        data.mocap_pos[1]=[x,y,.45]` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 25 | `        with viewer.lock():` | Viewer와 공유하는 모델 상태를 안전하게 변경합니다. |
| 26 | `            model.geom_rgba[gid]=[risk,1-risk,.1,1]` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 27 | `        mujoco.mj_step(model,data)` | 자동차 물리 시뮬레이션을 한 스텝 진행합니다. |
| 28 | `        rows.append({"time_s":float(data.time),"x_m":x,"y_m":y,` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 29 | `                     "distance_m":dist,"cross_track_error_m":error,` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 30 | `                     "risk":risk,"left_ctrl":float(data.ctrl[0]),"right_ctrl":float(data.ctrl[1])})` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 31 | `        viewer.sync(); time.sleep(model.opt.timestep)` | 물리 상태·화면·키 입력을 동기화합니다. |
| 32 | `report={` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 33 | `    "samples":len(rows),` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 34 | `    "minimum_distance_m":min(r["distance_m"] for r in rows) if rows else None,` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 35 | `    "maximum_cross_track_error_m":max(r["cross_track_error_m"] for r in rows) if rows else None,` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 36 | `    "maximum_risk":max(r["risk"] for r in rows) if rows else None}` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 37 | `p=save_json(report,"ex440_integrated_project_report.json")` | 프로젝트 진단 결과를 파일로 저장합니다. |
| 38 | `print(report,p)` | 센서값·거리·위험도·결과 경로를 출력합니다. |

## 확인 문제
1. 시각화용 위험도와 실제 안전정지 로직을 분리해야 하는 이유는 무엇인가?
2. 센서값·제어값·Viewer 화면을 같은 주기로 동기화해야 하는 이유는 무엇인가?
3. 실차 적용 전 어떤 fail-safe 검증이 필요한가?
