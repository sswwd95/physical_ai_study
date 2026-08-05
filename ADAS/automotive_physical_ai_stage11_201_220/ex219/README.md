# 예제 219 — 주행 이상 품질 리포트

## 학습 목표
자동차 센서 로그에서 **주행 이상 품질 리포트** 절차를 수행하고 ROS2 실시간 진단으로 연결하는 기초를 익힙니다.

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage11_201_220
conda activate auto_physical_ai
python ex219\main.py
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
| 1 | `import json` | 주행 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from common.anomaly_utils import load_data, confusion_counts, output_path` | 주행 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `df = load_data()` | 합성 자동차 주행 이상 로그를 읽습니다. |
| 4 | `truth = df["event_label"] != "NORMAL"` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 5 | `pred = (` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 6 | `    (df["accel_mps2"].abs() > 1.8) ¦` | 현재 주행 이상 분석 절차를 실행합니다. |
| 7 | `    (df["steering_deg"].abs() > 15) ¦` | 현재 주행 이상 분석 절차를 실행합니다. |
| 8 | `    (df["ttc_s"] < 2) ¦` | 현재 주행 이상 분석 절차를 실행합니다. |
| 9 | `    (df["motor_current_a"] > 7)` | 현재 주행 이상 분석 절차를 실행합니다. |
| 10 | `)` | 현재 주행 이상 분석 절차를 실행합니다. |
| 11 | `c = confusion_counts(truth,pred)` | 정답과 예측을 비교해 TP·FP·TN·FN을 계산합니다. |
| 12 | `report = {` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 13 | `    "rows": len(df),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 14 | `    "true_anomaly_samples": int(truth.sum()),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 15 | `    "predicted_anomaly_samples": int(pred.sum()),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 16 | `    **c,` | 현재 주행 이상 분석 절차를 실행합니다. |
| 17 | `    "precision": c["tp"]/max(1,c["tp"]+c["fp"]),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 18 | `    "recall": c["tp"]/max(1,c["tp"]+c["fn"]),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 19 | `}` | 현재 주행 이상 분석 절차를 실행합니다. |
| 20 | `path = output_path("ex219_anomaly_quality_report.json")` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 21 | `path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 22 | `print(report)` | 탐지 개수, 임계값, 평가 지표 또는 저장 경로를 출력합니다. |
| 23 | `print("saved:", path)` | 탐지 개수, 임계값, 평가 지표 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 샘플 단위 이상 탐지와 이벤트 구간 탐지의 차이는 무엇인가?
2. precision과 recall 중 안전 시스템에서 무엇을 더 우선할 수 있는가?
3. Isolation Forest의 contamination 값을 잘못 설정하면 어떤 문제가 생기는가?
