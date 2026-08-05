# 예제 150 — 자이로 바이어스 보정 적분

## 학습 목표
자동차와 TurtleBot3에 공통으로 사용되는 IMU·엔코더의 **자이로 바이어스 보정 적분** 원리를 익힙니다.

## 실행 방법
```bat
cd /d C:\work\automotive_physical_ai_stage8_141_160
conda activate auto_physical_ai
python ex150\main.py
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
| 4 | `bias = (df.loc[df["time_s"] < 5, "imu_gyroz_rps"] - df.loc[df["time_s"] < 5, "true_yaw_rate_rps"]).mean()` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 5 | `dt = df["time_s"].diff().fillna(0).to_numpy()` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 6 | `df["gyro_corrected"] = df["imu_gyroz_rps"] - bias` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 7 | `df["yaw_corrected"] = np.cumsum(df["gyro_corrected"].to_numpy() * dt)` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 8 | `print("estimated bias:", round(bias,6))` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |
| 9 | `print("corrected yaw RMSE:", round(rmse(df["yaw_corrected"], df["true_yaw_rad"]), 6))` | 기준값과 센서값 사이의 평균제곱근 오차를 계산합니다. |
| 10 | `path = output_path("ex150_corrected_yaw.csv")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 11 | `df[["time_s","true_yaw_rad","yaw_corrected"]].to_csv(path,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 12 | `print("saved:", path)` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 바이어스와 랜덤 노이즈의 차이는 무엇인가?
2. 자이로 바이어스가 자세 적분에 장시간 어떤 영향을 주는가?
3. 엔코더 분해능을 높이면 어떤 오차가 줄고 어떤 오차는 남는가?
