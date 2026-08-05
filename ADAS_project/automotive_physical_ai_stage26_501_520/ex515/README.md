# 예제 515 — Burger 휠 마찰 변화 실험

## 사전 준비
공식 저장소를 먼저 설치합니다.

```bat
scripts\01_clone_robotis_menagerie.bat
```

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage26_501_520
conda activate robotis_tb3_burger_viewer
python ex515\main.py
```

## 공식 모델 연결
이 예제는 ZIP에 모델 mesh를 재배포하지 않습니다. 공식 저장소의 `robotis_tb3/scene_turtlebot3_burger.xml`을 직접 읽으며, 해당 scene은 `turtlebot3_burger.xml`을 include합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 공식 Burger 모델과 Viewer 실행에 필요한 모듈을 불러옵니다. |
| 2 | `from common.tb3_burger_utils import load_tb3,set_wheels` | 공식 Burger 모델과 Viewer 실행에 필요한 모듈을 불러옵니다. |
| 3 | `mujoco,model,data,ids=load_tb3()` | 공식 scene 파일로 Burger 모델과 이름 ID를 로드합니다. |
| 4 | `left_body=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"wheel_left")` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 5 | `right_body=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"wheel_right")` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 6 | `wheel_geoms=[i for i in range(model.ngeom) if model.geom_bodyid[i] in (left_body,right_body)]` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 7 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 제어 루프와 병행하는 passive Viewer를 실행합니다. |
| 8 | `    while viewer.is_running() and data.time<16:` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 9 | `        if data.time>7:` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 10 | `            with viewer.lock():` | Viewer 공유 상태를 안전하게 변경합니다. |
| 11 | `                for gid in wheel_geoms:` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 12 | `                    model.geom_friction[gid,0]=0.2` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 13 | `        set_wheels(data,5,5)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 14 | `        mujoco.mj_step(model,data)` | MuJoCo 물리 시뮬레이션을 한 스텝 진행합니다. |
| 15 | `        viewer.sync()` | 물리 상태와 Viewer 화면·입력을 동기화합니다. |
| 16 | `        time.sleep(model.opt.timestep)` | 현재 Burger Viewer 실습 절차를 수행합니다. |

## 확인 문제
1. 공식 모델을 복사하지 않고 경로로 참조하는 이유는 무엇인가?
2. `wheel_left`, `wheel_right` actuator의 ctrlrange를 확인해야 하는 이유는 무엇인가?
3. scene 확장 시 원본 파일을 직접 수정하지 않는 것이 왜 유리한가?
