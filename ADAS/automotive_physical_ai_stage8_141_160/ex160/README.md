# 예제 160 — IMU·엔코더 노이즈 통합 분석

## 학습 목표
자동차와 TurtleBot3에 공통으로 사용되는 IMU·엔코더의 **IMU·엔코더 노이즈 통합 분석** 원리를 익힙니다.

## 실행 방법
```bat
cd /d C:\work\automotive_physical_ai_stage8_141_160
conda activate auto_physical_ai
python ex160\main.py
```

## 실무 연결
- IMU 가속도·자이로 → ROS2 `/imu`
- 바퀴 엔코더 위치·속도 → `/joint_states`
- 보정된 속도·자세 → `/odom`
- 실차에서는 센서 온도, 장착 방향, 시간 동기화, 진동, 바닥 슬립을 함께 고려합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import json, numpy as np` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `import matplotlib` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `matplotlib.use("Agg")` | 현재 센서 분석 절차를 실행합니다. |
| 4 | `import matplotlib.pyplot as plt` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `from common.sensor_utils import load_data, rmse, moving_average, output_path` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 6 | `df = load_data()` | 합성 IMU·엔코더 로그를 DataFrame으로 읽습니다. |
| 7 | `accel_bias = (df.loc[df["time_s"] < 5,"imu_ax_mps2"] - df.loc[df["time_s"] < 5,"true_accel_mps2"]).mean()` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 8 | `gyro_bias = (df.loc[df["time_s"] < 5,"imu_gyroz_rps"] - df.loc[df["time_s"] < 5,"true_yaw_rate_rps"]).mean()` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 9 | `df["accel_corrected"] = moving_average(df["imu_ax_mps2"] - accel_bias, 21)` | 이동평균으로 고주파 노이즈를 줄입니다. |
| 10 | `df["gyro_corrected"] = df["imu_gyroz_rps"] - gyro_bias` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 11 | `dt = df["time_s"].diff().fillna(0)` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 12 | `df["yaw_corrected"] = np.cumsum(df["gyro_corrected"] * dt)` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 13 | `df["slip_detected"] = (df["encoder_speed_mps"] - df["true_speed_mps"]).abs() > 0.03` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 14 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 15 | `csv_path = output_path("ex160_integrated_sensor_analysis.csv")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 16 | `df[["time_s","true_accel_mps2","accel_corrected","true_yaw_rad","yaw_corrected",` | 현재 센서 분석 절차를 실행합니다. |
| 17 | `    "true_speed_mps","encoder_speed_mps","slip_flag","slip_detected"]].to_csv(` | 분석 결과를 outputs 폴더에 저장합니다. |
| 18 | `        csv_path,index=False,encoding="utf-8-sig"` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 19 | `    )` | 현재 센서 분석 절차를 실행합니다. |
| 20 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 21 | `fig, axes = plt.subplots(3,1,figsize=(11,9),sharex=True)` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 22 | `axes[0].plot(df["time_s"],df["true_accel_mps2"],label="true")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 23 | `axes[0].plot(df["time_s"],df["accel_corrected"],alpha=.7,label="corrected")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 24 | `axes[0].legend(); axes[0].grid(True); axes[0].set_ylabel("Accel")` | 현재 센서 분석 절차를 실행합니다. |
| 25 | `axes[1].plot(df["time_s"],df["true_yaw_rad"],label="true")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 26 | `axes[1].plot(df["time_s"],df["yaw_corrected"],label="integrated")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 27 | `axes[1].legend(); axes[1].grid(True); axes[1].set_ylabel("Yaw")` | 현재 센서 분석 절차를 실행합니다. |
| 28 | `axes[2].plot(df["time_s"],df["true_speed_mps"],label="true")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 29 | `axes[2].plot(df["time_s"],df["encoder_speed_mps"],alpha=.6,label="encoder")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 30 | `axes[2].legend(); axes[2].grid(True); axes[2].set_ylabel("Speed"); axes[2].set_xlabel("Time (s)")` | 현재 센서 분석 절차를 실행합니다. |
| 31 | `plot_path = output_path("ex160_integrated_sensor_analysis.png")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 32 | `fig.tight_layout(); fig.savefig(plot_path,dpi=140); plt.close(fig)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 33 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 34 | `summary = {` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 35 | `    "accel_bias_estimate": float(accel_bias),` | 현재 센서 분석 절차를 실행합니다. |
| 36 | `    "gyro_bias_estimate": float(gyro_bias),` | 현재 센서 분석 절차를 실행합니다. |
| 37 | `    "corrected_accel_rmse": rmse(df["accel_corrected"],df["true_accel_mps2"]),` | 기준값과 센서값 사이의 평균제곱근 오차를 계산합니다. |
| 38 | `    "corrected_yaw_rmse": rmse(df["yaw_corrected"],df["true_yaw_rad"]),` | 기준값과 센서값 사이의 평균제곱근 오차를 계산합니다. |
| 39 | `    "slip_detection_samples": int(df["slip_detected"].sum()),` | 현재 센서 분석 절차를 실행합니다. |
| 40 | `}` | 현재 센서 분석 절차를 실행합니다. |
| 41 | `summary_path = output_path("ex160_summary.json")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 42 | `summary_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 43 | `print(summary)` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |
| 44 | `print("saved:", csv_path, plot_path, summary_path)` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 바이어스와 랜덤 노이즈의 차이는 무엇인가?
2. 자이로 바이어스가 자세 적분에 장시간 어떤 영향을 주는가?
3. 엔코더 분해능을 높이면 어떤 오차가 줄고 어떤 오차는 남는가?
