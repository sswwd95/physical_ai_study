# 예제 425 — 휠 슬립 시나리오 시각화

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage22_421_440
conda activate automotive_project_viewer
python ex425\main.py
```

## 프로젝트 연결
이 예제는 자동차 Physical AI 과정에서 다룬 센서 분석, 오도메트리, 휠 슬립, 경로 추종, 안전거리, 이상 탐지, 예지보전 또는 강화학습 결과를 MuJoCo Viewer로 확인합니다.

## 실행 조건
- Windows GUI·OpenGL 환경
- MuJoCo 3.6.0
- Viewer 창을 닫으면 실행 루프가 종료됩니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 프로젝트 Viewer에 필요한 모듈과 공통 함수를 불러옵니다. |
| 2 | `from common.project_viewer_utils import load_project,set_wheels` | 프로젝트 Viewer에 필요한 모듈과 공통 함수를 불러옵니다. |
| 3 | `mujoco,model,data,path=load_project()` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 4 | `with mujoco.viewer.launch_passive(model,data) as viewer:` | Python 제어 루프와 함께 실행되는 passive Viewer를 엽니다. |
| 5 | `    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT]=True` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 6 | `    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTFORCE]=True` | 제어값, 상태값, 위험도 또는 진단값을 계산합니다. |
| 7 | `    while viewer.is_running() and data.time<12:` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |
| 8 | `        if data.time<5:set_wheels(data,10,10)` | 좌우 바퀴 속도 명령을 안전 범위로 제한해 적용합니다. |
| 9 | `        else:set_wheels(data,15,4)` | 좌우 바퀴 속도 명령을 안전 범위로 제한해 적용합니다. |
| 10 | `        mujoco.mj_step(model,data)` | 자동차 물리 시뮬레이션을 한 스텝 진행합니다. |
| 11 | `        viewer.sync()` | 물리 상태·화면·키 입력을 동기화합니다. |
| 12 | `        time.sleep(model.opt.timestep)` | 현재 자동차 프로젝트 통합 절차를 실행합니다. |

## 확인 문제
1. 시각화용 위험도와 실제 안전정지 로직을 분리해야 하는 이유는 무엇인가?
2. 센서값·제어값·Viewer 화면을 같은 주기로 동기화해야 하는 이유는 무엇인가?
3. 실차 적용 전 어떤 fail-safe 검증이 필요한가?
