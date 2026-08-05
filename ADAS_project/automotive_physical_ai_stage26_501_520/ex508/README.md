# 예제 508 — 시간 기반 미션 명령 시퀀스

## 사전 준비
공식 저장소를 먼저 설치합니다.

```bat
scripts\01_clone_robotis_menagerie.bat
```

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage26_501_520
conda activate robotis_tb3_burger_viewer
python ex508\main.py
```

## 공식 모델 연결
이 예제는 ZIP에 모델 mesh를 재배포하지 않습니다. 공식 저장소의 `robotis_tb3/scene_turtlebot3_burger.xml`을 직접 읽으며, 해당 scene은 `turtlebot3_burger.xml`을 include합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.tb3_burger_utils import load_tb3,realtime_loop,set_wheels` | 공식 Burger 모델과 Viewer 실행에 필요한 모듈을 불러옵니다. |
| 2 | `mujoco,model,data,ids=load_tb3()` | 공식 scene 파일로 Burger 모델과 이름 ID를 로드합니다. |
| 3 | `def mission(model,data):` | 현재 Burger Viewer 실습 절차를 수행합니다. |
| 4 | `    t=data.time` | 제어값, 상태값, 경로 또는 평가값을 계산합니다. |
| 5 | `    if t<4:set_wheels(data,4,4)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 6 | `    elif t<7:set_wheels(data,-3,3)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 7 | `    elif t<11:set_wheels(data,4.5,4.5)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 8 | `    elif t<14:set_wheels(data,3,-3)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 9 | `    else:set_wheels(data,0,0)` | 공식 휠 actuator 범위 안에서 좌우 명령을 적용합니다. |
| 10 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 제어 루프와 병행하는 passive Viewer를 실행합니다. |
| 11 | `    realtime_loop(mujoco,model,data,viewer,16,mission)` | 현재 Burger Viewer 실습 절차를 수행합니다. |

## 확인 문제
1. 공식 모델을 복사하지 않고 경로로 참조하는 이유는 무엇인가?
2. `wheel_left`, `wheel_right` actuator의 ctrlrange를 확인해야 하는 이유는 무엇인가?
3. scene 확장 시 원본 파일을 직접 수정하지 않는 것이 왜 유리한가?
