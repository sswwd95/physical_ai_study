# 예제 248 — TTC 기반 위험확률 회귀

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage13_241_260
conda activate auto_physical_ai
python ex248\main.py
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
| 1 | `import pymc as pm` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 2 | `from common.risk_utils import load_data,standardize,sample_model,save_summary` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 3 | `df=load_data(); x=standardize(df["ttc_s"]).to_numpy(); y=df["risk_label"].to_numpy()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 4 | `with pm.Model() as model:` | 확률 모델 정의를 시작합니다. |
| 5 | `    a=pm.Normal("intercept",0,2)` | 회귀계수 또는 계층 효과의 정규 사전분포를 정의합니다. |
| 6 | `    b=pm.Normal("ttc_coef",0,2)` | 회귀계수 또는 계층 효과의 정규 사전분포를 정의합니다. |
| 7 | `    p=pm.math.sigmoid(a+b*x)` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 8 | `    pm.Bernoulli("obs",p=p,observed=y)` | 이상 여부 관측값의 베르누이 우도를 정의합니다. |
| 9 | `idata=sample_model(model)` | MCMC 샘플링으로 사후분포를 생성합니다. |
| 10 | `s,pth=save_summary(idata,["intercept","ttc_coef"],"ex248_ttc_logistic.csv")` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 11 | `print(s); print(pth)` | 추정값, 성능, 판정 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 위험확률과 위험 레이블의 차이는 무엇인가?
2. 미탐 비용을 높이면 최적 임계값은 어느 방향으로 움직이는가?
3. 운전자 계층 모델이 표본이 적은 운전자에게 주는 장점은 무엇인가?
