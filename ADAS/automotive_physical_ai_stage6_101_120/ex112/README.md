# 예제 112 — 제자리 회전 제어

## 학습 목표
MuJoCo에서 TurtleBot3 Burger 계열 모델을 안전하게 불러오고 **제자리 회전 제어** 작업을 수행합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage6_101_120
conda activate auto_physical_ai
python ex112\main.py
```

ROBOTIS 모델 저장소가 준비되어 있다면 먼저 환경변수를 지정합니다.

```bat
set ROBOTIS_MUJOCO_MENAGERIE=C:\work\robotis_mujoco_menagerie
```

## ROS2 연결
- 좌우 바퀴 명령 → `/cmd_vel`을 차동구동 바퀴 속도로 변환
- 베이스 위치·자세 → `/odom`
- 가속도·자이로 → `/imu`
- 바퀴 관절 위치·속도 → `/joint_states`

## 라인별 해설

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import mujoco` | MuJoCo 또는 공통 유틸리티를 불러옵니다. |
| 2 | `from common.mujoco_utils import load_model_and_data` | MuJoCo 또는 공통 유틸리티를 불러옵니다. |
| 3 | `_, model, data = load_model_and_data()` | XML 모델을 읽고 시뮬레이션 상태 객체를 만듭니다. |
| 4 | `if model.nu < 2:` | 현재 실습 절차를 실행합니다. |
| 5 | `    raise RuntimeError("두 개 이상의 바퀴 액추에이터가 필요합니다.")` | 현재 실습 절차를 실행합니다. |
| 6 | `data.ctrl[0] = -6.0` | 좌우 바퀴 액추에이터에 제어 명령을 입력합니다. |
| 7 | `data.ctrl[1] = 6.0` | 좌우 바퀴 액추에이터에 제어 명령을 입력합니다. |
| 8 | `for _ in range(300):` | 현재 실습 절차를 실행합니다. |
| 9 | `    mujoco.mj_step(model, data)` | MuJoCo 물리 시뮬레이션을 한 스텝 진행합니다. |
| 10 | `print("base quaternion:", data.qpos[3:7].copy())` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |
| 11 | `print("controls:", data.ctrl.copy())` | 좌우 바퀴 액추에이터에 제어 명령을 입력합니다. |

## 확인 문제
1. 선택한 XML에서 좌우 바퀴 액추에이터 이름은 무엇인가?
2. `model.nu`와 `data.ctrl` 길이는 왜 같은가?
3. 실차와 시뮬레이션의 바퀴 반지름·차축 간격이 다르면 어떤 오차가 생기는가?
