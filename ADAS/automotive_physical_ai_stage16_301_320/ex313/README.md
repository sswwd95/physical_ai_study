# 예제 313 — 각속도 PID 방향 제어

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage16_301_320
conda activate auto_physical_ai
python ex313\main.py
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
| 1 | `from common.control_utils import PID, simulate_first_order, error_metrics, output_path` | 제어 실습에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `pid=PID(2.0,0.8,0.15,output_limit=2.5,integral_limit=2.0)` | 비례·적분·미분 게인과 출력 제한을 가진 제어기를 만듭니다. |
| 3 | `df=simulate_first_order(pid,target=0.7,tau=.40)` | 교육용 1차 시스템에서 폐루프 제어 응답을 계산합니다. |
| 4 | `print(error_metrics(df))` | 제어 성능과 저장 경로를 출력합니다. |
| 5 | `p=output_path("ex313_yaw_rate_pid.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")` | 제어 로그·그래프·진단 결과를 저장합니다. |

## 확인 문제
1. Ki를 지나치게 크게 설정하면 어떤 현상이 생기는가?
2. 출력 포화가 있을 때 안티와인드업이 필요한 이유는 무엇인가?
3. 제어 주기가 길어지면 미분항과 안정성에 어떤 영향이 생기는가?
