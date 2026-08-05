# 예제 339 — MuJoCo 모델 경로추종 연계 스모크 테스트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage17_321_340
conda activate auto_physical_ai
python ex339\main.py
```

## 핵심 개념
- 최근접점: 현재 차량과 가장 가까운 경로 웨이포인트
- 횡방향 오차: 경로 좌우 방향으로 벗어난 거리
- 방향오차: 차량 방향과 경로 진행방향의 차이
- Pure Pursuit: 앞쪽 목표점을 바라보도록 곡률 계산
- Stanley: 방향오차와 횡오차를 함께 사용
- 곡률 기반 속도 제한: 급커브에서 속도를 낮추는 안전 전략

## ROS2 연결
- 경로 입력: `nav_msgs/Path`
- 차량 상태: `nav_msgs/Odometry`
- 속도 명령: `geometry_msgs/Twist`
- 경로 이탈·제어 포화: `/diagnostics`

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.path_tracking import MODEL_PATH` | 경로 추종에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `try:` | 현재 경로 추종 절차를 실행합니다. |
| 3 | `    import mujoco` | 경로 추종에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `except ImportError:` | 현재 경로 추종 절차를 실행합니다. |
| 5 | `    print("MuJoCo is not installed. Install environment.yml first.")` | 목표점, 오차, 성능 또는 저장 경로를 출력합니다. |
| 6 | `else:` | 현재 경로 추종 절차를 실행합니다. |
| 7 | `    model=mujoco.MjModel.from_xml_path(str(MODEL_PATH))` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 8 | `    data=mujoco.MjData(model)` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 9 | `    data.ctrl[:2]=[5.0,7.0]` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 10 | `    for _ in range(200):` | 현재 경로 추종 절차를 실행합니다. |
| 11 | `        mujoco.mj_step(model,data)` | MuJoCo 물리 시뮬레이션을 한 스텝 진행합니다. |
| 12 | `    print("model:",MODEL_PATH)` | 목표점, 오차, 성능 또는 저장 경로를 출력합니다. |
| 13 | `    print("time:",data.time)` | 목표점, 오차, 성능 또는 저장 경로를 출력합니다. |
| 14 | `    print("base qpos:",data.qpos[:7])` | 목표점, 오차, 성능 또는 저장 경로를 출력합니다. |

## 확인 문제
1. Pure Pursuit의 lookahead가 너무 작으면 어떤 현상이 생기는가?
2. Stanley gain을 크게 하면 횡오차와 조향 진동은 어떻게 변하는가?
3. 급커브에서 속도 제한이 필요한 이유는 무엇인가?
