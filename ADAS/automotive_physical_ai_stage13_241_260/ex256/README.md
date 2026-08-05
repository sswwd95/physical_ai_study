# 예제 256 — 확률 임계값별 비용 평가

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage13_241_260
conda activate auto_physical_ai
python ex256\main.py
```

첫 PyMC 실행은 컴파일 때문에 시간이 더 걸릴 수 있습니다.

## 핵심 개념
위험을 0 또는 1로만 판단하지 않고 사후 위험확률로 표현합니다.
미탐 비용과 오탐 비용을 다르게 설정하면 안전 요구에 맞는 경고 임계값을 선택할 수 있습니다.

## ROS2 연결
- 센서 입력: `/odom`, `/imu`, `/scan`, 모터 진단
- 출력: 위험확률, 위험등급, 권장 감속 또는 정지 플래그
- 진단: `/diagnostics` 또는 사용자 정의 `DrivingRisk` 메시지

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 2 | `from common.risk_utils import load_data,classification_metrics,output_path` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 3 | `df=load_data(); prob=df["true_risk_probability"].to_numpy(); y=df["risk_label"].to_numpy()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 4 | `rows=[]` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 5 | `false_negative_cost=10` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 6 | `false_positive_cost=2` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 7 | `for th in [.1,.2,.3,.4,.5,.6,.7,.8,.9]:` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 8 | `    m=classification_metrics(y,prob,th)` | 임계값에 따른 분류 성능과 비용을 계산합니다. |
| 9 | `    m["cost"]=m["fn"]*false_negative_cost+m["fp"]*false_positive_cost` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 10 | `    rows.append(m)` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 11 | `result=pd.DataFrame(rows).sort_values("cost")` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 12 | `pth=output_path("ex256_threshold_cost.csv"); result.to_csv(pth,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 13 | `print(result.head()); print(pth)` | 추정값, 성능, 판정 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 위험확률과 위험 레이블의 차이는 무엇인가?
2. 미탐 비용을 높이면 최적 임계값은 어느 방향으로 움직이는가?
3. 운전자 계층 모델이 표본이 적은 운전자에게 주는 장점은 무엇인가?
