# 예제 354 — 안전거리 기반 속도 제한

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage18_341_360
conda activate auto_physical_ai
python ex354\main.py
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
| 1 | `import numpy as np` | 안전거리·충돌 위험 분석에 필요한 라이브러리를 불러옵니다. |
| 2 | `from common.safety_utils import load_data,output_path` | 안전거리·충돌 위험 분석에 필요한 라이브러리를 불러옵니다. |
| 3 | `df=load_data()` | 합성 충돌 위험 로그를 읽습니다. |
| 4 | `margin=df["distance_m"]-df["safe_distance_m"]` | 반응거리·제동거리·여유거리를 합산합니다. |
| 5 | `df["speed_limit_mps"]=np.where(margin>=0,df["ego_speed_mps"],np.clip(df["ego_speed_mps"]+0.35*margin,0,df["ego_speed_mps"]))` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 6 | `p=output_path("ex354_safety_speed_limit.csv")` | 거리, TTC, 감속, 회피 또는 평가값을 계산합니다. |
| 7 | `df[["time_s","distance_m","safe_distance_m","speed_limit_mps"]].to_csv(p,index=False,encoding="utf-8-sig")` | 반응거리·제동거리·여유거리를 합산합니다. |
| 8 | `print(df["speed_limit_mps"].describe())` | 위험 수치, 성능 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 마찰계수가 낮아지면 제동거리는 어떻게 변하는가?
2. TTC만 사용하면 안전하지 않을 수 있는 상황은 무엇인가?
3. 긴급정지와 일반 감속을 분리해야 하는 이유는 무엇인가?
