# 예제 317 — 샘플링 주기 영향 비교

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage16_301_320
conda activate auto_physical_ai
python ex317\main.py
```

## 핵심 개념
- P: 현재 오차에 비례한 제어
- I: 누적 오차를 줄여 정상상태 오차 개선
- D: 오차 변화율을 이용해 급격한 변화를 완화
- 포화: 액추에이터가 낼 수 있는 최대 명령 제한
- 데드존: 작은 명령에는 액추에이터가 반응하지 않는 구간
- 안티와인드업: 포화 중 적분항이 과도하게 쌓이는 현상 방지

## ROS2 연결
- 목표 선속도·각속도: `/cmd_vel`
- 바퀴 속도: `/joint_states`
- 실제 선속도·각속도와 자세: `/odom`
- 제어기 상태와 포화 경고: `/diagnostics`

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | 제어 실습에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from common.control_utils import PID, simulate_first_order, error_metrics, output_path` | 제어 실습에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `rows=[]` | 목표값, 제어값, 상태값 또는 평가 지표를 계산합니다. |
| 4 | `for dt in [.1,.05,.02,.01]:` | 현재 PID 제어 절차를 실행합니다. |
| 5 | `    m=error_metrics(simulate_first_order(PID(1.5,.7,.1,2.0,2.0),1.0,dt=dt))` | 비례·적분·미분 게인과 출력 제한을 가진 제어기를 만듭니다. |
| 6 | `    rows.append({"dt_s":dt,**m})` | 현재 PID 제어 절차를 실행합니다. |
| 7 | `r=pd.DataFrame(rows)` | 목표값, 제어값, 상태값 또는 평가 지표를 계산합니다. |
| 8 | `p=output_path("ex317_sampling_period_comparison.csv"); r.to_csv(p,index=False,encoding="utf-8-sig")` | 제어 로그·그래프·진단 결과를 저장합니다. |
| 9 | `print(r)` | 제어 성능과 저장 경로를 출력합니다. |

## 확인 문제
1. Ki를 지나치게 크게 설정하면 어떤 현상이 생기는가?
2. 출력 포화가 있을 때 안티와인드업이 필요한 이유는 무엇인가?
3. 제어 주기가 길어지면 미분항과 안정성에 어떤 영향이 생기는가?
