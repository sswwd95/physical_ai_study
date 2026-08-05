# 예제 147 — 가속도 노이즈 히스토그램

## 학습 목표
자동차와 TurtleBot3에 공통으로 사용되는 IMU·엔코더의 **가속도 노이즈 히스토그램** 원리를 익힙니다.

## 실행 방법
```bat
cd /d C:\work\automotive_physical_ai_stage8_141_160
conda activate auto_physical_ai
python ex147\main.py
```

## 실무 연결
- IMU 가속도·자이로 → ROS2 `/imu`
- 바퀴 엔코더 위치·속도 → `/joint_states`
- 보정된 속도·자세 → `/odom`
- 실차에서는 센서 온도, 장착 방향, 시간 동기화, 진동, 바닥 슬립을 함께 고려합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import matplotlib` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `matplotlib.use("Agg")` | 현재 센서 분석 절차를 실행합니다. |
| 3 | `import matplotlib.pyplot as plt` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from common.sensor_utils import load_data, output_path` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `df = load_data()` | 합성 IMU·엔코더 로그를 DataFrame으로 읽습니다. |
| 6 | `error = df["imu_ax_mps2"] - df["true_accel_mps2"]` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 7 | `fig, ax = plt.subplots(figsize=(8,4))` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 8 | `ax.hist(error, bins=60)` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 9 | `ax.set_title("Accelerometer Error Distribution")` | 현재 센서 분석 절차를 실행합니다. |
| 10 | `ax.set_xlabel("Error (m/s^2)")` | 현재 센서 분석 절차를 실행합니다. |
| 11 | `ax.set_ylabel("Frequency")` | 현재 센서 분석 절차를 실행합니다. |
| 12 | `ax.grid(True)` | 현재 센서 분석 절차를 실행합니다. |
| 13 | `path = output_path("ex147_accel_error_histogram.png")` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 14 | `fig.tight_layout(); fig.savefig(path,dpi=140); plt.close(fig)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 15 | `print("saved:", path)` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 바이어스와 랜덤 노이즈의 차이는 무엇인가?
2. 자이로 바이어스가 자세 적분에 장시간 어떤 영향을 주는가?
3. 엔코더 분해능을 높이면 어떤 오차가 줄고 어떤 오차는 남는가?
