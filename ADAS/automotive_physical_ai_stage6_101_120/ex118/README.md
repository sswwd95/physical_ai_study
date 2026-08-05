# 예제 118 — 시뮬레이션 상태 CSV 기록

## 학습 목표
MuJoCo에서 TurtleBot3 Burger 계열 모델을 안전하게 불러오고 **시뮬레이션 상태 CSV 기록** 작업을 수행합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage6_101_120
conda activate auto_physical_ai
python ex118\main.py
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
| 1 | `import csv, mujoco` | MuJoCo 또는 공통 유틸리티를 불러옵니다. |
| 2 | `from common.mujoco_utils import load_model_and_data, output_path` | MuJoCo 또는 공통 유틸리티를 불러옵니다. |
| 3 | `_, model, data = load_model_and_data()` | XML 모델을 읽고 시뮬레이션 상태 객체를 만듭니다. |
| 4 | `path = output_path("ex118_simulation_log.csv")` | 모델 정보, 제어값, 센서값 또는 결과 변수를 계산합니다. |
| 5 | `with path.open("w", newline="", encoding="utf-8-sig") as f:` | 모델 정보, 제어값, 센서값 또는 결과 변수를 계산합니다. |
| 6 | `    writer = csv.writer(f)` | 모델 정보, 제어값, 센서값 또는 결과 변수를 계산합니다. |
| 7 | `    writer.writerow(["time_s","x","y","z","left_ctrl","right_ctrl"])` | 시뮬레이션 결과를 파일에 기록합니다. |
| 8 | `    data.ctrl[:2] = [6.0, 6.0]` | 좌우 바퀴 액추에이터에 제어 명령을 입력합니다. |
| 9 | `    for step in range(500):` | 현재 실습 절차를 실행합니다. |
| 10 | `        mujoco.mj_step(model, data)` | MuJoCo 물리 시뮬레이션을 한 스텝 진행합니다. |
| 11 | `        if step % 10 == 0:` | 모델 정보, 제어값, 센서값 또는 결과 변수를 계산합니다. |
| 12 | `            writer.writerow([data.time, *data.qpos[:3], *data.ctrl[:2]])` | 좌우 바퀴 액추에이터에 제어 명령을 입력합니다. |
| 13 | `print("saved:", path)` | 모델 구조나 실행 결과를 콘솔에 출력합니다. |

## 확인 문제
1. 선택한 XML에서 좌우 바퀴 액추에이터 이름은 무엇인가?
2. `model.nu`와 `data.ctrl` 길이는 왜 같은가?
3. 실차와 시뮬레이션의 바퀴 반지름·차축 간격이 다르면 어떤 오차가 생기는가?
