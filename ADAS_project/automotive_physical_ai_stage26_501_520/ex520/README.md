# 예제 520 — robotis_tb3 Burger 프로젝트 통합 Viewer

## 사전 준비
공식 저장소를 먼저 설치합니다.

```bat
scripts\01_clone_robotis_menagerie.bat
```

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage26_501_520
conda activate robotis_tb3_burger_viewer
python ex520\main.py
```

## 공식 모델 연결
이 예제는 ZIP에 모델 mesh를 재배포하지 않습니다. 공식 저장소의 `robotis_tb3/scene_turtlebot3_burger.xml`을 직접 읽으며, 해당 scene은 `turtlebot3_burger.xml`을 include합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,json,pandas as pd` | 공식 Burger 모델과 Viewer 실행에 필요한 모듈을 불러옵니다. |
| 2 | `from common.tb3_burger_utils import load_tb3,set_wheels,base_pose,output_path` | 공식 Burger 모델과 Viewer 실행에 필요한 모듈을 불러옵니다. |
| 3 | `mujoco,model,data,ids=load_tb3()` | 공식 scene 파일로 Burger 모델과 이름 ID를 로드합니다. |
| 4 | `rows=[]; emergency_stops=0` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 5 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 제어 루프와 병행하는 passive Viewer를 실행합니다. |
| 6 | `    viewer.cam.type=mujoco.mjtCamera.mjCAMERA_TRACKING` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 7 | `    viewer.cam.trackbodyid=ids["base_body"]` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 8 | `    viewer.cam.distance=2.0` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 9 | `    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT]=True` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 10 | `    while viewer.is_running() and data.time<20:` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 11 | `        pose=base_pose(data)` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 12 | `        virtual_obstacle_x=2.0` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 13 | `        distance=virtual_obstacle_x-pose["x_m"]` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 14 | `        if distance<.35:` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 15 | `            set_wheels(data,0,0); emergency_stops+=1` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 16 | `        elif data.time<6:set_wheels(data,4.5,4.5)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 17 | `        elif data.time<10:set_wheels(data,-3.0,3.0)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 18 | `        elif data.time<16:set_wheels(data,4.0,4.5)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 19 | `        else:set_wheels(data,0,0)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 20 | `        mujoco.mj_step(model,data)` | MuJoCo 물리 시뮬레이션을 한 스텝 진행합니다. |
| 21 | `        rows.append({"time_s":float(data.time),**pose,"virtual_distance_m":distance,` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 22 | `                     "left_ctrl":float(data.ctrl[0]),"right_ctrl":float(data.ctrl[1])})` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 23 | `        viewer.sync()` | 물리 상태와 Viewer 화면·입력을 동기화합니다. |
| 24 | `        time.sleep(model.opt.timestep)` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 25 | `csv_path=output_path("ex520_tb3_integrated_log.csv")` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 26 | `pd.DataFrame(rows).to_csv(csv_path,index=False,encoding="utf-8-sig")` | 실습 로그 또는 리포트를 저장합니다. |
| 27 | `report={"samples":len(rows),"emergency_stop_samples":emergency_stops,` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 28 | `        "final_pose":base_pose(data),"official_scene":str(model.names)}` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 29 | `json_path=output_path("ex520_tb3_integrated_report.json")` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 30 | `json_path.write_text(json.dumps(report,ensure_ascii=False,indent=2,default=str),encoding="utf-8")` | 실습 로그 또는 리포트를 저장합니다. |
| 31 | `print(csv_path,json_path)` | 모델 구조, 상태 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 공식 모델을 복사하지 않고 경로로 참조하는 이유는 무엇인가?
2. `wheel_left`, `wheel_right` actuator의 ctrlrange를 확인해야 하는 이유는 무엇인가?
3. scene 확장 시 원본 파일을 직접 수정하지 않는 것이 왜 유리한가?
