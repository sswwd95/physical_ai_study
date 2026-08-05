# 예제 275 — 특징 중요도 분석

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage14_261_280
conda activate auto_physical_ai
python ex275\main.py
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
| 1 | `import pandas as pd` | 부품 상태 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.ensemble import RandomForestClassifier` | 부품 상태 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from common.health_utils import load_data,FEATURES,output_path` | 부품 상태 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `df=load_data()` | 합성 차량 부품 상태 로그를 읽습니다. |
| 5 | `model=RandomForestClassifier(n_estimators=180,class_weight="balanced",random_state=42,n_jobs=1)` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 6 | `model.fit(df[FEATURES],df["failure_label"])` | 훈련 데이터로 예측 모델을 학습합니다. |
| 7 | `imp=pd.DataFrame({"feature":FEATURES,"importance":model.feature_importances_}).sort_values("importance",ascending=False)` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 8 | `p=output_path("ex275_feature_importance.csv"); imp.to_csv(p,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 9 | `print(imp)` | 상태 지표, 성능, RUL 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 임계값 기반 경고와 추세 기반 경고의 차이는 무엇인가?
2. RUL 단순 선형추정이 부정확해지는 경우는 무엇인가?
3. 건강도 점수의 가중치를 차량별로 다시 정해야 하는 이유는 무엇인가?
