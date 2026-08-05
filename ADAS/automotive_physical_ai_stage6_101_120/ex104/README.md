# 예제 104 — 모델 기본 크기 정보

## 학습 목표
MuJoCo에서 TurtleBot3 Burger 계열 모델을 안전하게 불러오고 **모델 기본 크기 정보** 작업을 수행합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage6_101_120
conda activate auto_physical_ai
python ex104\main.py
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
| 1 | `from common.mujoco_utils import load_model_and_data` | MuJoCo 또는 공통 유틸리티를 불러옵니다. |
| 2 | `_, model, _ = load_model_and_data()` | XML 모델을 읽고 시뮬레이션 상태 객체를 만듭니다. |
| 3 | `print("bodies:", model.nbody)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |
| 4 | `print("joints:", model.njnt)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |
| 5 | `print("geoms:", model.ngeom)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |
| 6 | `print("sites:", model.nsite)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |
| 7 | `print("actuators:", model.nu)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |
| 8 | `print("sensors:", model.nsensor)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |

## 확인 문제
1. 선택한 XML에서 좌우 바퀴 액추에이터 이름은 무엇인가?
2. `model.nu`와 `data.ctrl` 길이는 왜 같은가?
3. 실차와 시뮬레이션의 바퀴 반지름·차축 간격이 다르면 어떤 오차가 생기는가?
