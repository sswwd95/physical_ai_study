# 예제 280 — 차량 부품 상태·예지보전 통합 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage14_261_280
conda activate auto_physical_ai
python ex280\main.py
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
| 1 | `import json` | 부품 상태 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 2 | `from sklearn.ensemble import RandomForestClassifier` | 부품 상태 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 3 | `from sklearn.metrics import classification_report` | 부품 상태 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 4 | `from common.health_utils import load_data,FEATURES,output_path` | 부품 상태 분석에 필요한 라이브러리와 공통 함수를 불러옵니다. |
| 5 | `df=load_data(); split=int(len(df)*.7)` | 합성 차량 부품 상태 로그를 읽습니다. |
| 6 | `model=RandomForestClassifier(n_estimators=220,class_weight="balanced",random_state=42,n_jobs=1)` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 7 | `model.fit(df.iloc[:split][FEATURES],df.iloc[:split]["failure_label"])` | 훈련 데이터로 예측 모델을 학습합니다. |
| 8 | `prob=model.predict_proba(df.iloc[split:][FEATURES])[:,1]` | 건강도·고장 상태 또는 확률을 예측합니다. |
| 9 | `pred=(prob>=0.35).astype(int)` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 10 | `report=classification_report(df.iloc[split:]["failure_label"],pred,output_dict=True,zero_division=0)` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 11 | `result=df.iloc[split:][["time_s","health_score","failure_label"]].copy()` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 12 | `result["failure_probability"]=prob; result["predicted_failure"]=pred` | 건강도·고장 상태 또는 확률을 예측합니다. |
| 13 | `csv_path=output_path("ex280_failure_predictions.csv"); result.to_csv(csv_path,index=False,encoding="utf-8-sig")` | 건강도·고장 상태 또는 확률을 예측합니다. |
| 14 | `last=df.iloc[-1]` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 15 | `summary={` | 상태지표, 임계값, 예측값 또는 유지보수 점수를 계산합니다. |
| 16 | `"final_health_score":float(last["health_score"]),` | 현재 예지보전 분석 절차를 실행합니다. |
| 17 | `"final_motor_temp_c":float(last["motor_temp_c"]),` | 현재 예지보전 분석 절차를 실행합니다. |
| 18 | `"final_vibration_g":float(last["bearing_vibration_g"]),` | 현재 예지보전 분석 절차를 실행합니다. |
| 19 | `"final_battery_voltage_v":float(last["battery_voltage_v"]),` | 현재 예지보전 분석 절차를 실행합니다. |
| 20 | `"failure_samples":int(df["failure_label"].sum()),` | 현재 예지보전 분석 절차를 실행합니다. |
| 21 | `"classification_report":report}` | 현재 예지보전 분석 절차를 실행합니다. |
| 22 | `json_path=output_path("ex280_integrated_report.json"); json_path.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 23 | `print(summary)` | 상태 지표, 성능, RUL 또는 저장 경로를 출력합니다. |
| 24 | `print(csv_path,json_path)` | 상태 지표, 성능, RUL 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 임계값 기반 경고와 추세 기반 경고의 차이는 무엇인가?
2. RUL 단순 선형추정이 부정확해지는 경우는 무엇인가?
3. 건강도 점수의 가중치를 차량별로 다시 정해야 하는 이유는 무엇인가?
