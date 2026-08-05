# 예제 215 — Isolation Forest 기초 탐지

## 학습 목표
자동차 센서 로그에서 **Isolation Forest 기초 탐지** 절차를 수행하고 ROS2 실시간 진단으로 연결하는 기초를 익힙니다.

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage11_201_220
conda activate auto_physical_ai
python ex215\main.py
```

## 실무 연결
- 속도·자세 → `/odom`
- 가속도·자이로 → `/imu`
- 전방 거리 → `/scan` 또는 거리 센서 토픽
- 탐지 결과 → `/diagnostics` 또는 사용자 정의 위험 경고 토픽
- 규칙 기반 탐지는 설명이 쉽고 빠르지만 차량·노면별 튜닝이 필요합니다.
- Isolation Forest는 복합 패턴을 찾지만 정상 데이터 구성과 contamination 설정에 민감합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from sklearn.ensemble import IsolationForest` | 주행 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from common.anomaly_utils import load_data, output_path` | 주행 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `df = load_data()` | 합성 자동차 주행 이상 로그를 읽습니다. |
| 4 | `features = df[["speed_mps","accel_mps2","steering_deg","ttc_s","motor_current_a"]]` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 5 | `model = IsolationForest(contamination=0.10, random_state=42)` | 비지도 이상 탐지 모델을 생성하거나 학습합니다. |
| 6 | `df["iforest_anomaly"] = model.fit_predict(features) == -1` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 7 | `path = output_path("ex215_isolation_forest.csv")` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 8 | `df[df["iforest_anomaly"]].to_csv(path,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 9 | `print("detected:", int(df["iforest_anomaly"].sum()))` | 탐지 개수, 임계값, 평가 지표 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 샘플 단위 이상 탐지와 이벤트 구간 탐지의 차이는 무엇인가?
2. precision과 recall 중 안전 시스템에서 무엇을 더 우선할 수 있는가?
3. Isolation Forest의 contamination 값을 잘못 설정하면 어떤 문제가 생기는가?
