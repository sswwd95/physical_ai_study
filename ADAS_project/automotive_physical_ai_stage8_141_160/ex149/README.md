# 예제 149 — 자이로 적분 자세 오차

## 학습 목표
자동차와 TurtleBot3에 공통으로 사용되는 IMU·엔코더의 **자이로 적분 자세 오차** 원리를 익힙니다.

## 실행 방법
```bat
cd /d C:\work\automotive_physical_ai_stage8_141_160
conda activate auto_physical_ai
python ex149\main.py
```

## 실무 연결
- IMU 가속도·자이로 → ROS2 `/imu`
- 바퀴 엔코더 위치·속도 → `/joint_states`
- 보정된 속도·자세 → `/odom`
- 실차에서는 센서 온도, 장착 방향, 시간 동기화, 진동, 바닥 슬립을 함께 고려합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import numpy as np` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from common.sensor_utils import load_data, rmse, output_path` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `df = load_data()` | 합성 IMU·엔코더 로그를 DataFrame으로 읽습니다. |
| 4 | `dt = df["time_s"].diff().fillna(0).to_numpy()` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 5 | `df["yaw_from_gyro"] = np.cumsum(df["imu_gyroz_rps"].to_numpy() * dt)` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 6 | `df["yaw_error_rad"] = df["yaw_from_gyro"] - df["true_yaw_rad"]` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 7 | `print("final yaw error:", round(df["yaw_error_rad"].iloc[-1], 6))` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |
| 8 | `print("yaw RMSE:", round(rmse(df["yaw_from_gyro"], df["true_yaw_rad"]), 6))` | 기준값과 센서값 사이의 평균제곱근 오차를 계산합니다. |
| 9 | `path = output_path("ex149_gyro_integrated_yaw.csv")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 10 | `df[["time_s","true_yaw_rad","yaw_from_gyro","yaw_error_rad"]].to_csv(path,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 11 | `print("saved:", path)` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 바이어스와 랜덤 노이즈의 차이는 무엇인가?
2. 자이로 바이어스가 자세 적분에 장시간 어떤 영향을 주는가?
3. 엔코더 분해능을 높이면 어떤 오차가 줄고 어떤 오차는 남는가?
