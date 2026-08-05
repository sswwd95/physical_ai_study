# 예제 278 — 예지보전 우선순위 점수

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage14_261_280
conda activate auto_physical_ai
python ex278\main.py
```

## 실무 연결
- 모터 상태 → 모터 전류·온도 진단 토픽
- 배터리 상태 → 전압·내부저항·SOC 관련 토픽
- 베어링·휠 상태 → 진동과 마찰 진단
- 통합 경고 → `/diagnostics`
- 잔여수명은 정비 계획 참고값이며 안전 정지 판단을 단독으로 대체할 수 없습니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.health_utils import load_data,output_path` | 부품 상태 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `df=load_data()` | 합성 차량 부품 상태 로그를 읽습니다. |
| 3 | `last=df.iloc[-1]` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 4 | `scores={` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 5 | `"motor":max(0,(last["motor_temp_c"]-55)/20)*40+max(0,(last["motor_current_a"]-4)/3)*20,` | 현재 예지보전 분석 절차를 실행합니다. |
| 6 | `"bearing":max(0,(last["bearing_vibration_g"]-0.25)/0.25)*60,` | 현재 예지보전 분석 절차를 실행합니다. |
| 7 | `"battery":max(0,(12.2-last["battery_voltage_v"])/0.5)*30+max(0,(last["battery_internal_resistance_ohm"]-0.06)/0.03)*40,` | 현재 예지보전 분석 절차를 실행합니다. |
| 8 | `"wheel":max(0,(last["wheel_friction_index"]-0.15)/0.08)*40}` | 현재 예지보전 분석 절차를 실행합니다. |
| 9 | `ranking=sorted(scores.items(),key=lambda x:x[1],reverse=True)` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 10 | `p=output_path("ex278_maintenance_priority.json")` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 11 | `p.write_text(__import__("json").dumps({"scores":scores,"ranking":ranking},indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 12 | `print(ranking)` | 상태 지표, 성능, RUL 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 임계값 기반 경고와 추세 기반 경고의 차이는 무엇인가?
2. RUL 단순 선형추정이 부정확해지는 경우는 무엇인가?
3. 건강도 점수의 가중치를 차량별로 다시 정해야 하는 이유는 무엇인가?
