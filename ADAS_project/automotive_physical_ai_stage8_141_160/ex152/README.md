# 예제 152 — 엔코더 분해능 계산

## 학습 목표
자동차와 TurtleBot3에 공통으로 사용되는 IMU·엔코더의 **엔코더 분해능 계산** 원리를 익힙니다.

## 실행 방법
```bat
cd /d C:\work\automotive_physical_ai_stage8_141_160
conda activate auto_physical_ai
python ex152\main.py
```

## 실무 연결
- IMU 가속도·자이로 → ROS2 `/imu`
- 바퀴 엔코더 위치·속도 → `/joint_states`
- 보정된 속도·자세 → `/odom`
- 실차에서는 센서 온도, 장착 방향, 시간 동기화, 진동, 바닥 슬립을 함께 고려합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import math` | 센서 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `wheel_radius_m = 0.033` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 3 | `ticks_per_rev = 4096` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 4 | `distance_per_tick = 2 * math.pi * wheel_radius_m / ticks_per_rev` | 센서 오차, 보정값, 적분 결과 또는 탐지 조건을 계산합니다. |
| 5 | `print("distance per tick (m):", distance_per_tick)` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |
| 6 | `print("distance per tick (mm):", distance_per_tick * 1000)` | 바이어스, 오차, 품질 지표 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 바이어스와 랜덤 노이즈의 차이는 무엇인가?
2. 자이로 바이어스가 자세 적분에 장시간 어떤 영향을 주는가?
3. 엔코더 분해능을 높이면 어떤 오차가 줄고 어떤 오차는 남는가?
