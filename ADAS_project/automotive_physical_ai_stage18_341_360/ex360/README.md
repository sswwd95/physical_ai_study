# 예제 360 — 장애물·안전거리 통합 제어 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage18_341_360
conda activate auto_physical_ai
python ex360\main.py
```

## 핵심 개념
- 상대속도: 자차 속도와 선행차 속도의 차이
- TTC: 현재 접근속도가 유지될 때 충돌까지 남은 시간
- 반응거리: 위험 인지 후 제동 전까지 이동하는 거리
- 제동거리: 제동 시작 후 정지까지 필요한 거리
- 안전거리: 반응거리 + 제동거리 + 여유거리
- 히스테리시스: 경고 ON·OFF 기준을 다르게 두어 채터링 방지

## ROS2 연결
- 장애물 거리: `/scan`, 거리센서 또는 객체 추적 토픽
- 자차 속도: `/odom`
- 감속·정지 명령: `/cmd_vel`
- 위험 상태: `/diagnostics` 또는 사용자 정의 안전 메시지

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import json,numpy as np` | 안전거리·충돌 위험 분석에 필요한 라이브러리를 불러옵니다. |
| 2 | `from common.safety_utils import load_data,hysteresis_alarm,confusion_counts,output_path` | 안전거리·충돌 위험 분석에 필요한 라이브러리를 불러옵니다. |
| 3 | `df=load_data()` | 합성 충돌 위험 로그를 읽습니다. |
| 4 | `df["warning"]=hysteresis_alarm(df["ttc_s"],2.0,3.0)` | 경고가 빠르게 켜졌다 꺼지는 채터링을 줄입니다. |
| 5 | `df["emergency_stop"]=(df["ttc_s"]<1.0)¦(df["distance_m"]<2.5)` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 6 | `ratio=np.clip(df["distance_m"]/df["safe_distance_m"],0,1.2)` | 반응거리·제동거리·여유거리를 합산합니다. |
| 7 | `df["target_speed_mps"]=df["ego_speed_mps"]*np.clip(ratio,0,1)` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 8 | `df["decel_cmd_mps2"]=np.clip(df["target_speed_mps"]-df["ego_speed_mps"],-4.0,0.0)` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 9 | `df["avoidance_yaw_rate_rps"]=np.where(` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 10 | `    (df["warning"]) & (~df["emergency_stop"]),` | 현재 안전 제어 절차를 실행합니다. |
| 11 | `    np.clip(-0.05*df["obstacle_angle_deg"],-1.0,1.0),` | 현재 안전 제어 절차를 실행합니다. |
| 12 | `    0.0` | 현재 안전 제어 절차를 실행합니다. |
| 13 | `)` | 현재 안전 제어 절차를 실행합니다. |
| 14 | `pred=df["warning"]¦df["emergency_stop"]` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 15 | `counts=confusion_counts(df["risk_label"],pred)` | 위험 탐지 성능을 평가합니다. |
| 16 | `csv_path=output_path("ex360_integrated_safety_control.csv")` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 17 | `df.to_csv(csv_path,index=False,encoding="utf-8-sig")` | 분석·제어 결과를 outputs 폴더에 저장합니다. |
| 18 | `report={` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 19 | `    "rows":len(df),` | 현재 안전 제어 절차를 실행합니다. |
| 20 | `    "warning_samples":int(df["warning"].sum()),` | 현재 안전 제어 절차를 실행합니다. |
| 21 | `    "emergency_stop_samples":int(df["emergency_stop"].sum()),` | 현재 안전 제어 절차를 실행합니다. |
| 22 | `    "max_deceleration_mps2":float(df["decel_cmd_mps2"].min()),` | 현재 안전 제어 절차를 실행합니다. |
| 23 | `    "max_abs_avoidance_yaw_rate_rps":float(df["avoidance_yaw_rate_rps"].abs().max()),` | 현재 안전 제어 절차를 실행합니다. |
| 24 | `    "confusion":counts,` | 현재 안전 제어 절차를 실행합니다. |
| 25 | `    "precision":counts["tp"]/max(1,counts["tp"]+counts["fp"]),` | 현재 안전 제어 절차를 실행합니다. |
| 26 | `    "recall":counts["tp"]/max(1,counts["tp"]+counts["fn"])` | 현재 안전 제어 절차를 실행합니다. |
| 27 | `}` | 현재 안전 제어 절차를 실행합니다. |
| 28 | `json_path=output_path("ex360_integrated_report.json")` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 29 | `json_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석·제어 결과를 outputs 폴더에 저장합니다. |
| 30 | `print(report)` | 위험 수치, 성능 또는 저장 경로를 출력합니다. |
| 31 | `print(csv_path,json_path)` | 위험 수치, 성능 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 마찰계수가 낮아지면 제동거리는 어떻게 변하는가?
2. TTC만 사용하면 안전하지 않을 수 있는 상황은 무엇인가?
3. 긴급정지와 일반 감속을 분리해야 하는 이유는 무엇인가?
