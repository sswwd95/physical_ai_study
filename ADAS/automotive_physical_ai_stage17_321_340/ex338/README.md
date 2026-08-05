# 예제 338 — 추종 궤적 시각화

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage17_321_340
conda activate auto_physical_ai
python ex338\main.py
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
| 1 | `import matplotlib` | 경로 추종에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `matplotlib.use("Agg")` | 현재 경로 추종 절차를 실행합니다. |
| 3 | `import matplotlib.pyplot as plt` | 경로 추종에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from common.path_tracking import *` | 경로 추종에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `path=load_path("path_sine.csv")` | CSV 웨이포인트 경로를 읽습니다. |
| 6 | `def pp(path,x,y,yaw,speed): return pure_pursuit_control(path,x,y,yaw,speed,.8)` | 룩어헤드 목표점 기반 조향 명령을 계산합니다. |
| 7 | `df=simulate_tracker(path,pp,.6,23)` | 평면 차량 모델로 경로 추종을 시뮬레이션합니다. |
| 8 | `fig,ax=plt.subplots(figsize=(10,5))` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 9 | `ax.plot(path["x_m"],path["y_m"],label="reference")` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 10 | `ax.plot(df["x_m"],df["y_m"],label="tracked")` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 11 | `ax.set_aspect("equal",adjustable="box"); ax.grid(True); ax.legend()` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 12 | `p=output_path("ex338_tracking_trajectory.png")` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 13 | `fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)` | 경로 추종 결과를 저장합니다. |
| 14 | `print(p)` | 목표점, 오차, 성능 또는 저장 경로를 출력합니다. |

## 확인 문제
1. Pure Pursuit의 lookahead가 너무 작으면 어떤 현상이 생기는가?
2. Stanley gain을 크게 하면 횡오차와 조향 진동은 어떻게 변하는가?
3. 급커브에서 속도 제한이 필요한 이유는 무엇인가?
