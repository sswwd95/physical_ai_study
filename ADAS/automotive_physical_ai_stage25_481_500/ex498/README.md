# 예제 498 — 전복 위험도 색상 시각화

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage25_481_500
conda activate automotive_dynamics_viewer
python ex498\main.py
```

## 신규 학습영역
이 예제는 기존 제어·교통·V2X·센서 고장주입과 달리 차량의 서스펜션, 롤·피치, 적재 편심, 타이어, 경사로, 연석, 견인 안정성과 전복 위험을 다룹니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,math` | 차량 동역학 Viewer용 모듈을 불러옵니다. |
| 2 | `from common.dynamics_utils import load_project,set_drive,chassis_rpy` | 차량 동역학 Viewer용 모듈을 불러옵니다. |
| 3 | `mujoco,model,data,plan=load_project()` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 4 | `gid=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_GEOM,"chassis_geom")` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 5 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | 동역학 시험 루프와 함께 Viewer를 실행합니다. |
| 6 | `    while viewer.is_running() and data.time<18:` | 현재 차량 동역학 시험 절차를 수행합니다. |
| 7 | `        diff=7*math.sin(data.time*1.5)` | 동역학 상태, 위험도 또는 시험 명령을 계산합니다. |
| 8 | `        set_drive(data,13-diff,13+diff,13-diff,13+diff)` | 4개 바퀴 구동 명령을 설정합니다. |
| 9 | `        mujoco.mj_step(model,data)` | 차량 동역학 물리 상태를 한 스텝 진행합니다. |
| 10 | `        roll=abs(chassis_rpy(data)[0]); risk=min(1,roll/.5)` | 차체의 롤·피치·요 각도를 계산합니다. |
| 11 | `        with viewer.lock(): model.geom_rgba[gid]=[risk,1-risk,.1,1]` | 모델 물성이나 색상을 안전하게 변경합니다. |
| 12 | `        viewer.sync(); time.sleep(model.opt.timestep)` | 물리 상태와 Viewer 표시를 동기화합니다. |

## 확인 문제
1. 서스펜션 강성과 감쇠가 승차감과 안정성에 어떤 영향을 주는가?
2. 적재물 위치가 롤·피치와 축하중에 어떤 영향을 주는가?
3. 트레일러 스웨이와 전복 위험을 줄이려면 어떤 제한이 필요한가?
