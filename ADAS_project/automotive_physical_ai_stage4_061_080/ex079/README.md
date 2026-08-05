# 예제 079 — 구간별 통계 리포트

## 학습 목표
자동차 센서 로그에서 **구간별 통계 리포트** 작업을 수행하고, 결과를 ROS2 주행 데이터 분석에 연결합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage4_061_080
conda activate auto_physical_ai
python ex079\main.py
```

## 입력과 출력
- 입력: `data/vehicle_sensor_log.csv`
- 출력: 실행 후 `outputs` 폴더에 CSV, PNG 또는 JSON 생성
- 원본 데이터는 수정하지 않습니다.

## 실무 연결
이 분석은 ROS2 Humble에서 `/odom`, `/imu`, 거리 센서, 모터 상태 토픽을 기록한 후
주행 안전성, 센서 관계, 상태 구간을 검토하는 기초 절차에 해당합니다.

## 라인별 해설

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.data_utils import load_vehicle_data, output_path` | 실습에 필요한 라이브러리 또는 공통 함수를 불러옵니다. |
| 2 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 3 | `df = load_vehicle_data()` | 공통 자동차 센서 CSV를 DataFrame으로 읽습니다. |
| 4 | `df["window_10s"] = (df["time_s"] // 10).astype(int)` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 5 | `report = df.groupby("window_10s").agg(` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 6 | `    start_time_s=("time_s", "min"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 7 | `    end_time_s=("time_s", "max"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 8 | `    mean_speed_mps=("speed_mps", "mean"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 9 | `    max_speed_mps=("speed_mps", "max"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 10 | `    min_distance_m=("front_distance_m", "min"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 11 | `    max_abs_accel=("accel_mps2", lambda s: s.abs().max()),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 12 | `    max_abs_steering=("steering_deg", lambda s: s.abs().max()),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 13 | `    mean_current_a=("motor_current_a", "mean"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 14 | `)` | 현재 분석 절차를 실행합니다. |
| 15 | `path = output_path("ex079_window_statistics.csv")` | 결과가 공통 outputs 폴더에 저장되도록 경로를 만듭니다. |
| 16 | `report.to_csv(path, encoding="utf-8-sig")` | 분석 결과를 파일로 저장합니다. |
| 17 | `print(report.round(3))` | 실행 결과와 핵심 요약값을 콘솔에 출력합니다. |
| 18 | `print(f"saved: {path}")` | 실행 결과와 핵심 요약값을 콘솔에 출력합니다. |

## 확인 문제
1. 현재 사용한 임계값은 어떤 차량과 주행 환경을 가정하는가?
2. 센서 주기가 10 Hz가 아니라면 구간 지속시간 계산을 어떻게 바꿔야 하는가?
3. 분석 결과를 ROS2 노드의 경고 토픽으로 연결하려면 어떤 입력과 출력이 필요한가?
