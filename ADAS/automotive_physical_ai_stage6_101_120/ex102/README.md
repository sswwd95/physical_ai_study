# 예제 102 — TurtleBot3 모델 경로 탐색

## 학습 목표
MuJoCo에서 TurtleBot3 Burger 계열 모델을 안전하게 불러오고 **TurtleBot3 모델 경로 탐색** 작업을 수행합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage6_101_120
conda activate auto_physical_ai
python ex102\main.py
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
| 1 | `from common.mujoco_utils import find_tb3_xml` | MuJoCo 또는 공통 유틸리티를 불러옵니다. |
| 2 | `path = find_tb3_xml()` | 모델 정보, 제어값, 센서값 또는 결과 변수를 계산합니다. |
| 3 | `print("selected model:", path)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |
| 4 | `print("exists:", path.exists())` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |
| 5 | `print("using fallback:", "tb3_burger_training.xml" in path.name)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |

## 확인 문제
1. 선택한 XML에서 좌우 바퀴 액추에이터 이름은 무엇인가?
2. `model.nu`와 `data.ctrl` 길이는 왜 같은가?
3. 실차와 시뮬레이션의 바퀴 반지름·차축 간격이 다르면 어떤 오차가 생기는가?
