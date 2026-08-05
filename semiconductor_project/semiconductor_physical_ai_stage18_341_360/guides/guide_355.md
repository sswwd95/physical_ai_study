# 실습 355 — uncertainty_review_zone

## 1. 학습 목표
중간 확률 구간을 재검사 대상으로 분리합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
위험확률 0.35~0.75를 재검사 구간으로 설정하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage18
python examples\ex355_uncertainty_review_zone.py
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
| 14 | `safe_df=pd.read_csv(DATA_FILE)` | 안전 의사결정 센서 스트림을 읽습니다. |
| 15 | `features=["temperature_c","pressure_pa","vibration_rms_g","gas_flow_sccm","particle_count","door_closed","cooling_ok","vacuum_ok"]` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 16 | `X=safe_df[features]; y=safe_df["anomaly_type"].ne("normal").astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 17 | `m=RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 18 | `m.fit(X,y); prob=m.predict_proba(X)[:,1]` | 과거 데이터로 위험 분류 모델을 학습합니다. |
| 19 | `safe_df["risk_probability"]=prob` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 20 | `safe_df["review_required"]=safe_df["risk_probability"].between(.35,.75)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 21 | `print("재검사 대상:",int(safe_df["review_required"].sum()))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 자동 정지 조건이 안전 규정과 일치하는가?
2. 경보 미탐과 오탐의 비용을 별도로 평가했는가?
3. 센서 불확실성·통신지연·수동 개입 절차를 반영했는가?