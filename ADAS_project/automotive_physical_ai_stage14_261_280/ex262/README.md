# 예제 262 — 모터 온도 추세 분석

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage14_261_280
conda activate auto_physical_ai
python ex262\main.py
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
| 3 | `df["motor_temp_ma"]=df["motor_temp_c"].rolling(50,min_periods=1).mean()` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 4 | `p=output_path("ex262_motor_temp_trend.csv")` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 5 | `df[["time_s","motor_temp_c","motor_temp_ma"]].to_csv(p,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 6 | `print(df[["motor_temp_c","motor_temp_ma"]].tail())` | 상태 지표, 성능, RUL 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 임계값 기반 경고와 추세 기반 경고의 차이는 무엇인가?
2. RUL 단순 선형추정이 부정확해지는 경우는 무엇인가?
3. 건강도 점수의 가중치를 차량별로 다시 정해야 하는 이유는 무엇인가?
