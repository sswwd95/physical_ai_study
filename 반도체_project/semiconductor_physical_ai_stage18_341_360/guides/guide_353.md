# 실습 353 — random_forest_risk_model

## 1. 학습 목표
Random Forest로 위험상태 확률을 예측합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForest로 이상상태를 분류하고 성능을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage18
python examples\ex353_random_forest_risk_model.py
```

## 4. 예상 결과
요청한 이상 대응·안전 의사결정 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리를 불러옵니다. |
| 14 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리를 불러옵니다. |
| 15 | `from sklearn.metrics import classification_report` | 필요한 라이브러리를 불러옵니다. |
| 16 | `safe_df=pd.read_csv(DATA_FILE)` | 안전 의사결정 센서 스트림을 읽습니다. |
| 17 | `features=["temperature_c","pressure_pa","vibration_rms_g","gas_flow_sccm","particle_count","door_closed","cooling_ok","vacuum_ok"]` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 18 | `X=safe_df[features]; y=safe_df["anomaly_type"].ne("normal").astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 19 | `Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 20 | `model=RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 21 | `model.fit(Xtr,ytr)` | 과거 데이터로 위험 분류 모델을 학습합니다. |
| 22 | `pred=model.predict(Xte)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 23 | `print(classification_report(yte,pred,zero_division=0))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 자동 정지 조건이 안전 규정과 일치하는가?
2. 경보 미탐과 오탐의 비용을 별도로 평가했는가?
3. 센서 불확실성·통신지연·수동 개입 절차를 반영했는가?