# 예제 140 — 차동구동·오도메트리 통합 분석

## 학습 목표
TurtleBot3 Burger 차동구동 모델에서 **차동구동·오도메트리 통합 분석** 원리를 이해하고 Python으로 확인합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage7_121_140
conda activate auto_physical_ai
python ex140\main.py
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
| 1 | `import json, pandas as pd` | 분석에 필요한 라이브러리와 공통 운동학 함수를 불러옵니다. |
| 2 | `import matplotlib` | 분석에 필요한 라이브러리와 공통 운동학 함수를 불러옵니다. |
| 3 | `matplotlib.use("Agg")` | 현재 실습 절차를 실행합니다. |
| 4 | `import matplotlib.pyplot as plt` | 분석에 필요한 라이브러리와 공통 운동학 함수를 불러옵니다. |
| 5 | `from common.diff_drive import integrate_odometry, path_length, output_path, twist_to_wheels` | 분석에 필요한 라이브러리와 공통 운동학 함수를 불러옵니다. |
| 6 | `cmd = pd.read_csv("data/drive_commands.csv")` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 7 | `commands = [(r.linear_mps, r.angular_rps, r.duration_s, r.mode) for r in cmd.itertuples(index=False)]` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 8 | `df = integrate_odometry(commands, dt=0.05)` | 속도 명령을 시간에 따라 적분해 로봇 자세를 계산합니다. |
| 9 | `wheel_rows = []` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 10 | `for r in cmd.itertuples(index=False):` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 11 | `    left, right = twist_to_wheels(r.linear_mps, r.angular_rps)` | 선속도와 각속도를 좌우 바퀴 각속도로 변환합니다. |
| 12 | `    wheel_rows.append([r.mode, r.linear_mps, r.angular_rps, left, right, r.duration_s])` | 현재 실습 절차를 실행합니다. |
| 13 | `wheel_df = pd.DataFrame(wheel_rows, columns=[` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 14 | `    "mode","linear_mps","angular_rps","left_rad_s","right_rad_s","duration_s"` | 현재 실습 절차를 실행합니다. |
| 15 | `])` | 현재 실습 절차를 실행합니다. |
| 16 | `traj_path = output_path("ex140_integrated_trajectory.csv")` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 17 | `wheel_path = output_path("ex140_wheel_commands.csv")` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 18 | `df.to_csv(traj_path,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 19 | `wheel_df.to_csv(wheel_path,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 20 | `fig, ax = plt.subplots(figsize=(6,6))` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 21 | `for mode, group in df.groupby("mode", sort=False):` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 22 | `    ax.plot(group["x_m"], group["y_m"], label=mode)` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 23 | `ax.set_aspect("equal", adjustable="box")` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 24 | `ax.set_xlabel("X (m)")` | 현재 실습 절차를 실행합니다. |
| 25 | `ax.set_ylabel("Y (m)")` | 현재 실습 절차를 실행합니다. |
| 26 | `ax.set_title("Integrated Differential Drive Analysis")` | 현재 실습 절차를 실행합니다. |
| 27 | `ax.grid(True)` | 현재 실습 절차를 실행합니다. |
| 28 | `ax.legend()` | 현재 실습 절차를 실행합니다. |
| 29 | `plot_path = output_path("ex140_integrated_trajectory.png")` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 30 | `fig.tight_layout()` | 현재 실습 절차를 실행합니다. |
| 31 | `fig.savefig(plot_path,dpi=140)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 32 | `plt.close(fig)` | 현재 실습 절차를 실행합니다. |
| 33 | `last = df.iloc[-1]` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 34 | `summary = {` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 35 | `    "path_length_m": path_length(df),` | 연속된 XY 위치 차이로 누적 이동거리를 계산합니다. |
| 36 | `    "final_pose": [float(last.x_m), float(last.y_m), float(last.yaw_rad)],` | 현재 실습 절차를 실행합니다. |
| 37 | `    "command_count": len(wheel_df),` | 현재 실습 절차를 실행합니다. |
| 38 | `    "trajectory_samples": len(df)` | 현재 실습 절차를 실행합니다. |
| 39 | `}` | 현재 실습 절차를 실행합니다. |
| 40 | `summary_path = output_path("ex140_summary.json")` | 운동학, 오도메트리 또는 오차 분석에 필요한 값을 계산합니다. |
| 41 | `summary_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 42 | `print(summary)` | 핵심 계산값과 저장 경로를 콘솔에 출력합니다. |
| 43 | `print("saved:", traj_path, wheel_path, plot_path, summary_path)` | 핵심 계산값과 저장 경로를 콘솔에 출력합니다. |

## 확인 문제
1. 바퀴 반지름이 실제보다 작게 설정되면 이동거리는 어떻게 추정되는가?
2. 좌우 바퀴 중심 간 거리가 틀리면 회전각에 어떤 오차가 생기는가?
3. 휠 슬립이 발생할 때 IMU와 오도메트리를 어떻게 함께 사용할 수 있는가?
