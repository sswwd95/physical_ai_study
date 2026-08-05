# 예제 499 — 차량 동역학 시험 로그 저장

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage25_481_500
conda activate automotive_dynamics_viewer
python ex499\main.py
```

## 신규 학습영역
이 예제는 기존 제어·교통·V2X·센서 고장주입과 달리 차량의 서스펜션, 롤·피치, 적재 편심, 타이어, 경사로, 연석, 견인 안정성과 전복 위험을 다룹니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,pandas as pd` | 차량 동역학 Viewer용 모듈을 불러옵니다. |
| 2 | `from common.dynamics_utils import load_project,set_all,chassis_rpy,suspension_positions,output_path` | 차량 동역학 Viewer용 모듈을 불러옵니다. |
| 3 | `mujoco,model,data,plan=load_project()` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 4 | `rows=[]` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 5 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 동역학 시험 루프와 함께 Viewer를 실행합니다. |
| 6 | `    while viewer.is_running() and data.time<15:` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 7 | `        set_all(data,10); mujoco.mj_step(model,data)` | 4개 바퀴 구동 명령을 설정합니다. |
| 8 | `        roll,pitch,yaw=chassis_rpy(data); susp=suspension_positions(model,data)` | 차체의 롤·피치·요 각도를 계산합니다. |
| 9 | `        rows.append([data.time,*data.qpos[:3],roll,pitch,yaw,*susp.values()])` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 10 | `        viewer.sync(); time.sleep(model.opt.timestep)` | 물리 상태와 Viewer 표시를 동기화합니다. |
| 11 | `p=output_path("ex499_dynamics_test_log.csv")` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 12 | `cols=["time_s","x_m","y_m","z_m","roll","pitch","yaw","fl","fr","rl","rr"]` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 13 | `pd.DataFrame(rows,columns=cols).to_csv(p,index=False)` | 시험 결과를 CSV 또는 JSON으로 저장합니다. |
| 14 | `print(p)` | 롤·피치·서스펜션·시험 결과를 출력합니다. |

## 확인 문제
1. 서스펜션 강성과 감쇠가 승차감과 안정성에 어떤 영향을 주는가?
2. 적재물 위치가 롤·피치와 축하중에 어떤 영향을 주는가?
3. 트레일러 스웨이와 전복 위험을 줄이려면 어떤 제한이 필요한가?
