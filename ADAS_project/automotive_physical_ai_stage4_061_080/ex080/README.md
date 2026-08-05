# 예제 080 — 통합 주행 구간 분석 대시보드

## 학습 목표
자동차 센서 로그에서 **통합 주행 구간 분석 대시보드** 작업을 수행하고, 결과를 ROS2 주행 데이터 분석에 연결합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage4_061_080
conda activate auto_physical_ai
python ex080\main.py
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
| 1 | `import matplotlib` | 실습에 필요한 라이브러리 또는 공통 함수를 불러옵니다. |
| 2 | `matplotlib.use("Agg")` | 현재 분석 절차를 실행합니다. |
| 3 | `import matplotlib.pyplot as plt` | 실습에 필요한 라이브러리 또는 공통 함수를 불러옵니다. |
| 4 | `import numpy as np` | 실습에 필요한 라이브러리 또는 공통 함수를 불러옵니다. |
| 5 | `from common.data_utils import load_vehicle_data, output_path` | 실습에 필요한 라이브러리 또는 공통 함수를 불러옵니다. |
| 6 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 7 | `df = load_vehicle_data()` | 공통 자동차 센서 CSV를 DataFrame으로 읽습니다. |
| 8 | `df["ttc_s"] = (df["front_distance_m"] / df["speed_mps"].clip(lower=0.5)).clip(upper=20)` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 9 | `df["risk_flag"] = (df["ttc_s"] < 2.0) & (df["speed_mps"] > 3.0)` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 10 | `df["state"] = np.select(` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 11 | `    [` | 현재 분석 절차를 실행합니다. |
| 12 | `        df["speed_mps"] < 0.5,` | 현재 분석 절차를 실행합니다. |
| 13 | `        df["accel_mps2"] >= 1.0,` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 14 | `        df["accel_mps2"] <= -1.0,` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 15 | `        df["steering_deg"].abs() >= 8,` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 16 | `    ],` | 현재 분석 절차를 실행합니다. |
| 17 | `    ["STOP", "ACCELERATE", "DECELERATE", "TURN"],` | 현재 분석 절차를 실행합니다. |
| 18 | `    default="CRUISE",` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 19 | `)` | 현재 분석 절차를 실행합니다. |
| 20 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 21 | `fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)` | 그래프 객체를 만들거나 축·제목·격자·저장 형식을 설정합니다. |
| 22 | `axes[0].plot(df["time_s"], df["speed_mps"])` | 현재 분석 절차를 실행합니다. |
| 23 | `axes[0].set_ylabel("Speed")` | 현재 분석 절차를 실행합니다. |
| 24 | `axes[0].grid(True)` | 현재 분석 절차를 실행합니다. |
| 25 | `axes[1].plot(df["time_s"], df["accel_mps2"])` | 현재 분석 절차를 실행합니다. |
| 26 | `axes[1].set_ylabel("Accel")` | 현재 분석 절차를 실행합니다. |
| 27 | `axes[1].grid(True)` | 현재 분석 절차를 실행합니다. |
| 28 | `axes[2].plot(df["time_s"], df["steering_deg"])` | 현재 분석 절차를 실행합니다. |
| 29 | `axes[2].set_ylabel("Steering")` | 현재 분석 절차를 실행합니다. |
| 30 | `axes[2].grid(True)` | 현재 분석 절차를 실행합니다. |
| 31 | `axes[3].plot(df["time_s"], df["ttc_s"])` | 현재 분석 절차를 실행합니다. |
| 32 | `axes[3].axhline(2.0, linestyle="--")` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 33 | `axes[3].set_ylabel("TTC")` | 현재 분석 절차를 실행합니다. |
| 34 | `axes[3].set_xlabel("Time (s)")` | 현재 분석 절차를 실행합니다. |
| 35 | `axes[3].grid(True)` | 현재 분석 절차를 실행합니다. |
| 36 | `fig.suptitle("Integrated Driving Analysis Dashboard")` | 그래프 객체를 만들거나 축·제목·격자·저장 형식을 설정합니다. |
| 37 | `fig.tight_layout()` | 그래프 객체를 만들거나 축·제목·격자·저장 형식을 설정합니다. |
| 38 | `dashboard_path = output_path("ex080_integrated_dashboard.png")` | 결과가 공통 outputs 폴더에 저장되도록 경로를 만듭니다. |
| 39 | `fig.savefig(dashboard_path, dpi=140)` | 그래프 객체를 만들거나 축·제목·격자·저장 형식을 설정합니다. |
| 40 | `plt.close(fig)` | 그래프 객체를 만들거나 축·제목·격자·저장 형식을 설정합니다. |
| 41 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 42 | `summary = {` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 43 | `    "samples": int(len(df)),` | 현재 분석 절차를 실행합니다. |
| 44 | `    "duration_s": float(df["time_s"].max()),` | 현재 분석 절차를 실행합니다. |
| 45 | `    "mean_speed_mps": float(df["speed_mps"].mean()),` | 현재 분석 절차를 실행합니다. |
| 46 | `    "max_speed_mps": float(df["speed_mps"].max()),` | 현재 분석 절차를 실행합니다. |
| 47 | `    "minimum_ttc_s": float(df["ttc_s"].min()),` | 현재 분석 절차를 실행합니다. |
| 48 | `    "risk_samples": int(df["risk_flag"].sum()),` | 현재 분석 절차를 실행합니다. |
| 49 | `    "state_counts": df["state"].value_counts().to_dict(),` | 현재 분석 절차를 실행합니다. |
| 50 | `}` | 현재 분석 절차를 실행합니다. |
| 51 | `summary_path = output_path("ex080_summary.json")` | 결과가 공통 outputs 폴더에 저장되도록 경로를 만듭니다. |
| 52 | `summary_path.write_text(` | 분석 결과를 파일로 저장합니다. |
| 53 | `    __import__("json").dumps(summary, ensure_ascii=False, indent=2),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 54 | `    encoding="utf-8"` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 55 | `)` | 현재 분석 절차를 실행합니다. |
| 56 | `print(summary)` | 실행 결과와 핵심 요약값을 콘솔에 출력합니다. |
| 57 | `print(f"saved: {dashboard_path}")` | 실행 결과와 핵심 요약값을 콘솔에 출력합니다. |
| 58 | `print(f"saved: {summary_path}")` | 실행 결과와 핵심 요약값을 콘솔에 출력합니다. |

## 확인 문제
1. 현재 사용한 임계값은 어떤 차량과 주행 환경을 가정하는가?
2. 센서 주기가 10 Hz가 아니라면 구간 지속시간 계산을 어떻게 바꿔야 하는가?
3. 분석 결과를 ROS2 노드의 경고 토픽으로 연결하려면 어떤 입력과 출력이 필요한가?
