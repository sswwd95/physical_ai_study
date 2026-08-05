# 예제 518 — 공식 Burger 모델에 프레임 센서 확장

## 사전 준비
공식 저장소를 먼저 설치합니다.

```bat
scripts\01_clone_robotis_menagerie.bat
```

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage26_501_520
conda activate robotis_tb3_burger_viewer
python ex518\main.py
```

## 공식 모델 연결
이 예제는 ZIP에 모델 mesh를 재배포하지 않습니다. 공식 저장소의 `robotis_tb3/scene_turtlebot3_burger.xml`을 직접 읽으며, 해당 scene은 `turtlebot3_burger.xml`을 include합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 공식 Burger 모델과 Viewer 실행에 필요한 모듈을 불러옵니다. |
| 2 | `from common.tb3_burger_utils import make_extension_scene,set_wheels` | 공식 Burger 모델과 Viewer 실행에 필요한 모듈을 불러옵니다. |
| 3 | `import mujoco,mujoco.viewer` | 공식 Burger 모델과 Viewer 실행에 필요한 모듈을 불러옵니다. |
| 4 | `scene=make_extension_scene(` | 공식 Burger 모델을 include하는 확장 scene을 생성합니다. |
| 5 | `    "ex518_sensor_scene.xml",` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 6 | `    extra_sensor='<framepos name="burger_position" objtype="body" objname="base"/><framequat name="burger_orientation" objtype="body" objname="base"/>'` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 7 | `)` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 8 | `model=mujoco.MjModel.from_xml_path(str(scene)); data=mujoco.MjData(model)` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 9 | `next_print=0` | 모델 구조, 상태 또는 저장 경로를 출력합니다. |
| 10 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 제어 루프와 병행하는 passive Viewer를 실행합니다. |
| 11 | `    while viewer.is_running() and data.time<10:` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 12 | `        set_wheels(data,4,4); mujoco.mj_step(model,data)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 13 | `        if data.time>=next_print:` | 모델 구조, 상태 또는 저장 경로를 출력합니다. |
| 14 | `            print(data.sensordata.copy()); next_print+=1` | 모델 구조, 상태 또는 저장 경로를 출력합니다. |
| 15 | `        viewer.sync(); time.sleep(model.opt.timestep)` | 물리 상태와 Viewer 화면·입력을 동기화합니다. |

## 확인 문제
1. 공식 모델을 복사하지 않고 경로로 참조하는 이유는 무엇인가?
2. `wheel_left`, `wheel_right` actuator의 ctrlrange를 확인해야 하는 이유는 무엇인가?
3. scene 확장 시 원본 파일을 직접 수정하지 않는 것이 왜 유리한가?
