# 예제 133 — 누적 이동거리 계산

## 학습 목표
TurtleBot3 Burger 차동구동 모델에서 **누적 이동거리 계산** 원리를 이해하고 Python으로 확인합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage7_121_140
conda activate auto_physical_ai
python ex133\main.py
```

## 핵심 공식

차동구동 선속도와 각속도:

```text
v = r × (ωR + ωL) / 2
ω = r × (ωR - ωL) / L
```

- `r`: 바퀴 반지름
- `L`: 좌우 바퀴 중심 간 거리
- `ωL`, `ωR`: 좌우 바퀴 각속도
- `v`: 로봇 선속도
- `ω`: 로봇 각속도

## ROS2 연결
- `/cmd_vel.linear.x` → 목표 선속도
- `/cmd_vel.angular.z` → 목표 각속도
- 좌우 바퀴 속도 → `/joint_states`
- 적분된 위치와 자세 → `/odom`
- 실제 시스템에서는 IMU와 휠 엔코더를 함께 융합해야 합니다.

## 라인별 해설

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | 분석에 필요한 라이브러리와 공통 운동학 함수를 불러옵니다. |
| 2 | `from common.diff_drive import integrate_odometry, path_length` | 분석에 필요한 라이브러리와 공통 운동학 함수를 불러옵니다. |
| 3 | `cmd = pd.read_csv("data/drive_commands.csv")` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 4 | `commands = [(r.linear_mps, r.angular_rps, r.duration_s, r.mode) for r in cmd.itertuples(index=False)]` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 5 | `df = integrate_odometry(commands, dt=0.05)` | 속도 명령을 시간에 따라 적분해 로봇 자세를 계산합니다. |
| 6 | `print("path length (m):", round(path_length(df), 4))` | 연속된 XY 위치 차이로 누적 이동거리를 계산합니다. |
| 7 | `print("final displacement (m):", round((df.iloc[-1].x_m**2 + df.iloc[-1].y_m**2)**0.5, 4))` | 핵심 계산값과 저장 경로를 콘솔에 출력합니다. |

## 확인 문제
1. 바퀴 반지름이 실제보다 작게 설정되면 이동거리는 어떻게 추정되는가?
2. 좌우 바퀴 중심 간 거리가 틀리면 회전각에 어떤 오차가 생기는가?
3. 휠 슬립이 발생할 때 IMU와 오도메트리를 어떻게 함께 사용할 수 있는가?
