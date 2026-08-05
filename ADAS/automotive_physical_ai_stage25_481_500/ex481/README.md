# 예제 481 — 차량 동역학 시험환경 Viewer

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage25_481_500
conda activate automotive_dynamics_viewer
python ex481\main.py
```

## 신규 학습영역
이 예제는 기존 제어·교통·V2X·센서 고장주입과 달리 차량의 서스펜션, 롤·피치, 적재 편심, 타이어, 경사로, 연석, 견인 안정성과 전복 위험을 다룹니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.dynamics_utils import load_project` | 차량 동역학 Viewer용 모듈을 불러옵니다. |
| 2 | `mujoco,model,data,plan=load_project()` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 3 | `print(plan)` | 롤·피치·서스펜션·시험 결과를 출력합니다. |
| 4 | `print("bodies",model.nbody,"joints",model.njnt,"sensors",model.nsensor)` | 롤·피치·서스펜션·시험 결과를 출력합니다. |
| 5 | `mujoco.viewer.launch(model,data)` | 현재 차량 동역학 시험 절차를 수행합니다. |

## 확인 문제
1. 서스펜션 강성과 감쇠가 승차감과 안정성에 어떤 영향을 주는가?
2. 적재물 위치가 롤·피치와 축하중에 어떤 영향을 주는가?
3. 트레일러 스웨이와 전복 위험을 줄이려면 어떤 제한이 필요한가?
