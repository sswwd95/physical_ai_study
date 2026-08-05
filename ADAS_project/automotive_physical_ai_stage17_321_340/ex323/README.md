# 예제 323 — 최근접 웨이포인트 탐색

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage17_321_340
conda activate auto_physical_ai
python ex323\main.py
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
| 1 | `from common.path_tracking import load_path, nearest_path_index` | 경로 추종에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `path=load_path("path_sine.csv")` | CSV 웨이포인트 경로를 읽습니다. |
| 3 | `for point in [(1.0,.8),(4.5,-.2),(9.0,1.5)]:` | 현재 경로 추종 절차를 실행합니다. |
| 4 | `    idx=nearest_path_index(path,*point)` | 차량과 가장 가까운 경로점을 찾습니다. |
| 5 | `    print(point,"->",idx,path.iloc[idx].to_dict())` | 목표점, 오차, 성능 또는 저장 경로를 출력합니다. |

## 확인 문제
1. Pure Pursuit의 lookahead가 너무 작으면 어떤 현상이 생기는가?
2. Stanley gain을 크게 하면 횡오차와 조향 진동은 어떻게 변하는가?
3. 급커브에서 속도 제한이 필요한 이유는 무엇인가?
