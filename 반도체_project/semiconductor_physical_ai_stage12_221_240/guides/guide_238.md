# 실습 238 — remaining_life_interval

## 1. 학습 목표
앙상블 기반 RUL 예측구간을 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
20개 Random Forest로 RUL 5·50·95% 구간을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage12
python examples\ex238_remaining_life_interval.py
```

## 4. 예상 결과
요청한 예지보전 분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "predictive_maintenance_rul.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 예지보전 분석 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 예지보전 분석 단계를 수행합니다. |
| 12 | `        "data/predictive_maintenance_rul.csv 파일이 없습니다."` | 예지보전 분석 단계를 수행합니다. |
| 13 | `    )` | 예지보전 분석 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `from sklearn.ensemble import RandomForestRegressor` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.model_selection import GroupShuffleSplit` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `pm_df=pd.read_csv(DATA_FILE)` | 예지보전용 CSV를 DataFrame으로 읽습니다. |
| 18 | `features=["cycle","temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count","health_index"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `X=pm_df[features]; y=pm_df["rul_cycles"]; groups=pm_df["equipment_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,y,groups))` | 학습과 평가 데이터를 분리합니다. |
| 21 | `preds=[]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `for seed in range(20):` | 여러 장비 또는 설정에 같은 작업을 반복합니다. |
| 23 | `    m=RandomForestRegressor(n_estimators=120,max_depth=12,min_samples_leaf=3,random_state=seed,n_jobs=-1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    m.fit(X.iloc[tr],y.iloc[tr]); preds.append(m.predict(X.iloc[te]))` | 학습 데이터로 모델을 학습합니다. |
| 25 | `mat=np.vstack(preds)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `out=pm_df.iloc[te][["equipment_id","cycle","rul_cycles"]].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `out["rul_p05"]=np.quantile(mat,.05,axis=0); out["rul_p50"]=np.quantile(mat,.5,axis=0); out["rul_p95"]=np.quantile(mat,.95,axis=0)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `out.to_csv(OUTPUT_DIR/"ex238_rul_intervals.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |
| 29 | `print(out.head(10).round(2))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. RUL 라벨은 실제 고장 또는 교체 시점과 어떻게 연결되었는가?
2. 장비 단위 데이터 누수를 방지했는가?
3. 정비 임계값은 비용과 안전을 함께 반영하는가?