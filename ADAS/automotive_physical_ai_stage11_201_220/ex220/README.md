# 예제 220 — 주행 상태·이상 탐지 통합 파이프라인

## 학습 목표
자동차 센서 로그에서 **주행 상태·이상 탐지 통합 파이프라인** 절차를 수행하고 ROS2 실시간 진단으로 연결하는 기초를 익힙니다.

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage11_201_220
conda activate auto_physical_ai
python ex220\main.py
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
| 2 | `import numpy as np` | 주행 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `import pandas as pd` | 주행 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from sklearn.ensemble import IsolationForest` | 주행 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `from common.anomaly_utils import load_data, confusion_counts, output_path` | 주행 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 6 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 7 | `df = load_data()` | 합성 자동차 주행 이상 로그를 읽습니다. |
| 8 | `df["driving_state"] = np.select(` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 9 | `    [` | 현재 주행 이상 분석 절차를 실행합니다. |
| 10 | `        df["speed_mps"] < 0.5,` | 현재 주행 이상 분석 절차를 실행합니다. |
| 11 | `        df["accel_mps2"] > 1.2,` | 현재 주행 이상 분석 절차를 실행합니다. |
| 12 | `        df["accel_mps2"] < -1.2,` | 현재 주행 이상 분석 절차를 실행합니다. |
| 13 | `        df["steering_deg"].abs() > 10,` | 현재 주행 이상 분석 절차를 실행합니다. |
| 14 | `    ],` | 현재 주행 이상 분석 절차를 실행합니다. |
| 15 | `    ["STOP","ACCELERATE","DECELERATE","TURN"],` | 현재 주행 이상 분석 절차를 실행합니다. |
| 16 | `    default="CRUISE"` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 17 | `)` | 현재 주행 이상 분석 절차를 실행합니다. |
| 18 | `df["rule_anomaly"] = (` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 19 | `    (df["accel_mps2"].abs() > 1.8) ¦` | 현재 주행 이상 분석 절차를 실행합니다. |
| 20 | `    (df["steering_deg"].abs() > 15) ¦` | 현재 주행 이상 분석 절차를 실행합니다. |
| 21 | `    (df["ttc_s"] < 2) ¦` | 현재 주행 이상 분석 절차를 실행합니다. |
| 22 | `    (df["motor_current_a"] > 7)` | 현재 주행 이상 분석 절차를 실행합니다. |
| 23 | `)` | 현재 주행 이상 분석 절차를 실행합니다. |
| 24 | `features = df[["speed_mps","accel_mps2","steering_deg","ttc_s","motor_current_a"]]` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 25 | `model = IsolationForest(contamination=0.10,random_state=42)` | 비지도 이상 탐지 모델을 생성하거나 학습합니다. |
| 26 | `df["iforest_anomaly"] = model.fit_predict(features) == -1` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 27 | `df["anomaly_score"] = -model.score_samples(features)` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 28 | `df["final_anomaly"] = df["rule_anomaly"] ¦ (` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 29 | `    df["iforest_anomaly"] & (df["anomaly_score"] > df["anomaly_score"].quantile(0.95))` | 현재 주행 이상 분석 절차를 실행합니다. |
| 30 | `)` | 현재 주행 이상 분석 절차를 실행합니다. |
| 31 | `csv_path = output_path("ex220_integrated_anomaly_result.csv")` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 32 | `df.to_csv(csv_path,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 33 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 34 | `truth = df["event_label"] != "NORMAL"` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 35 | `counts = confusion_counts(truth,df["final_anomaly"])` | 정답과 예측을 비교해 TP·FP·TN·FN을 계산합니다. |
| 36 | `summary = {` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 37 | `    "rows": len(df),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 38 | `    "state_counts": df["driving_state"].value_counts().to_dict(),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 39 | `    "rule_anomalies": int(df["rule_anomaly"].sum()),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 40 | `    "iforest_anomalies": int(df["iforest_anomaly"].sum()),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 41 | `    "final_anomalies": int(df["final_anomaly"].sum()),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 42 | `    "confusion": counts,` | 현재 주행 이상 분석 절차를 실행합니다. |
| 43 | `    "precision": counts["tp"]/max(1,counts["tp"]+counts["fp"]),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 44 | `    "recall": counts["tp"]/max(1,counts["tp"]+counts["fn"]),` | 현재 주행 이상 분석 절차를 실행합니다. |
| 45 | `}` | 현재 주행 이상 분석 절차를 실행합니다. |
| 46 | `json_path = output_path("ex220_integrated_summary.json")` | 주행 상태, 이상 조건, 위험 점수 또는 평가값을 계산합니다. |
| 47 | `json_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 48 | `print(summary)` | 탐지 개수, 임계값, 평가 지표 또는 저장 경로를 출력합니다. |
| 49 | `print("saved:", csv_path, json_path)` | 탐지 개수, 임계값, 평가 지표 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 샘플 단위 이상 탐지와 이벤트 구간 탐지의 차이는 무엇인가?
2. precision과 recall 중 안전 시스템에서 무엇을 더 우선할 수 있는가?
3. Isolation Forest의 contamination 값을 잘못 설정하면 어떤 문제가 생기는가?
