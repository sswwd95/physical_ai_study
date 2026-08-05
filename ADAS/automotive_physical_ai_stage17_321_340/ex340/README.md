# 예제 340 — 경로 추종 통합 비교 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage17_321_340
conda activate auto_physical_ai
python ex340\main.py
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
| 1 | `import json,pandas as pd` | 경로 추종에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from common.path_tracking import *` | 경로 추종에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `path=load_path("path_sine.csv")` | CSV 웨이포인트 경로를 읽습니다. |
| 4 | `def pp(path,x,y,yaw,speed): return pure_pursuit_control(path,x,y,yaw,speed,.8)` | 룩어헤드 목표점 기반 조향 명령을 계산합니다. |
| 5 | `def st(path,x,y,yaw,speed): return stanley_control(path,x,y,yaw,speed,1.2)` | 방향오차와 횡오차 기반 조향 명령을 계산합니다. |
| 6 | `pp_df=simulate_tracker(path,pp,.6,23)` | 평면 차량 모델로 경로 추종을 시뮬레이션합니다. |
| 7 | `st_df=simulate_tracker(path,st,.6,23)` | 평면 차량 모델로 경로 추종을 시뮬레이션합니다. |
| 8 | `pp_path=output_path("ex340_pure_pursuit_log.csv"); pp_df.to_csv(pp_path,index=False,encoding="utf-8-sig")` | 경로 추종 결과를 저장합니다. |
| 9 | `st_path=output_path("ex340_stanley_log.csv"); st_df.to_csv(st_path,index=False,encoding="utf-8-sig")` | 경로 추종 결과를 저장합니다. |
| 10 | `comparison=pd.DataFrame([` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 11 | `    {"controller":"pure_pursuit",**tracking_metrics(pp_df)},` | 횡방향 오차의 MAE·RMSE·최댓값을 계산합니다. |
| 12 | `    {"controller":"stanley",**tracking_metrics(st_df)}` | 횡방향 오차의 MAE·RMSE·최댓값을 계산합니다. |
| 13 | `])` | 현재 경로 추종 절차를 실행합니다. |
| 14 | `cmp_path=output_path("ex340_comparison.csv"); comparison.to_csv(cmp_path,index=False,encoding="utf-8-sig")` | 경로 추종 결과를 저장합니다. |
| 15 | `best=comparison.sort_values("rmse_cte_m").iloc[0]` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 16 | `report={` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 17 | `    "recommended_controller":str(best["controller"]),` | 현재 경로 추종 절차를 실행합니다. |
| 18 | `    "recommended_rmse_cte_m":float(best["rmse_cte_m"]),` | 현재 경로 추종 절차를 실행합니다. |
| 19 | `    "pure_pursuit":tracking_metrics(pp_df),` | 횡방향 오차의 MAE·RMSE·최댓값을 계산합니다. |
| 20 | `    "stanley":tracking_metrics(st_df)` | 횡방향 오차의 MAE·RMSE·최댓값을 계산합니다. |
| 21 | `}` | 현재 경로 추종 절차를 실행합니다. |
| 22 | `json_path=output_path("ex340_integrated_report.json")` | 경로점, 오차, 조향값 또는 평가값을 계산합니다. |
| 23 | `json_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")` | 경로 추종 결과를 저장합니다. |
| 24 | `print(report)` | 목표점, 오차, 성능 또는 저장 경로를 출력합니다. |
| 25 | `print(pp_path,st_path,cmp_path,json_path)` | 목표점, 오차, 성능 또는 저장 경로를 출력합니다. |

## 확인 문제
1. Pure Pursuit의 lookahead가 너무 작으면 어떤 현상이 생기는가?
2. Stanley gain을 크게 하면 횡오차와 조향 진동은 어떻게 변하는가?
3. 급커브에서 속도 제한이 필요한 이유는 무엇인가?
