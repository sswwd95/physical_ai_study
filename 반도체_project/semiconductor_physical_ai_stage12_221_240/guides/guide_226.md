# 실습 226 — group_train_test_split

## 1. 학습 목표
장비 단위 학습·평가 분할을 수행합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
equipment_id 단위 GroupShuffleSplit을 수행하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage12
python examples\ex226_group_train_test_split.py
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
| 15 | `from sklearn.model_selection import GroupShuffleSplit` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `pm_df=pd.read_csv(DATA_FILE)` | 예지보전용 CSV를 DataFrame으로 읽습니다. |
| 17 | `X=pm_df.drop(columns=["rul_cycles","failure_within_20","failed"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `y=pm_df["failure_within_20"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `groups=pm_df["equipment_id"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `split=GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42)` | 학습과 평가 데이터를 분리합니다. |
| 21 | `tr,te=next(split.split(X,y,groups))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `print("학습 장비:",sorted(groups.iloc[tr].unique()))` | 결과를 콘솔에 출력합니다. |
| 23 | `print("평가 장비:",sorted(groups.iloc[te].unique()))` | 결과를 콘솔에 출력합니다. |
| 24 | `print("교집합:",set(groups.iloc[tr]) & set(groups.iloc[te]))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. RUL 라벨은 실제 고장 또는 교체 시점과 어떻게 연결되었는가?
2. 장비 단위 데이터 누수를 방지했는가?
3. 정비 임계값은 비용과 안전을 함께 반영하는가?