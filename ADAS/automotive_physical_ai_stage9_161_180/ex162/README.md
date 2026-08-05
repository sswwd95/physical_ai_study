# 예제 162 — 가속도 바이어스 기술통계

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage9_161_180
conda activate auto_physical_ai
python ex162\main.py
```

첫 PyMC 실행은 컴파일 때문에 시간이 더 걸릴 수 있습니다.

## 핵심 개념
사전분포는 데이터 관측 전 가정, 우도는 모수에서 데이터가 생성될 가능성,
사후분포는 두 정보를 결합한 최종 불확실성입니다. R-hat과 ESS로 샘플링 품질을 점검합니다.

## ROS2 연결
추정 바이어스는 IMU 보정값으로, 사후분산은 `sensor_msgs/Imu` 공분산 설정의 참고값으로,
기준 초과 사후확률은 진단·정비 경고로 연결할 수 있습니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.bayes_utils import load_data` | 필요한 PyMC·ArviZ·공통 함수를 불러옵니다. |
| 2 | `df=load_data(); x=df["accel_measurement_mps2"]` | 관측값, 모수, 통계량 또는 판정값을 계산합니다. |
| 3 | `print(x.describe()); print("mean:",x.mean(),"std:",x.std())` | 핵심 추정값 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 사전분포가 지나치게 좁으면 어떤 편향이 생기는가?
2. 95% 신용구간은 어떻게 해석하는가?
3. R-hat과 ESS가 좋지 않을 때 무엇을 조정해야 하는가?
