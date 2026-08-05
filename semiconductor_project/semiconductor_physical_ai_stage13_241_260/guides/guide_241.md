# 실습 241 — lifetime_data_profile

## 1. 학습 목표
수명·검열·그룹 분포를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
설비 수명 데이터의 검열 비율, 챔버 유형별 수명, RUL 스냅샷 크기를 요약하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage13
python examples\ex241_lifetime_data_profile.py
```

## 4. 예상 결과
요청한 베이지안 수명·고장확률·RUL 분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 8 | `LIFE_FILE = ROOT / "data" / "bayesian_equipment_lifetime.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 9 | `RUL_FILE = ROOT / "data" / "bayesian_rul_snapshots.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 11 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `life_df = pd.read_csv(LIFE_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 14 | `rul_df = pd.read_csv(RUL_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 16 | `print("수명 데이터 크기:", life_df.shape)` | 결과를 콘솔에 출력합니다. |
| 17 | `print("RUL 스냅샷 크기:", rul_df.shape)` | 결과를 콘솔에 출력합니다. |
| 18 | `print("\n검열 분포:")` | 결과를 콘솔에 출력합니다. |
| 19 | `print(life_df["event_observed"].value_counts())` | 결과를 콘솔에 출력합니다. |
| 20 | `print("\n챔버별 관측 수명:")` | 결과를 콘솔에 출력합니다. |
| 21 | `print(life_df.groupby("chamber_type")["observed_cycles"].describe().round(2))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 검열 데이터가 왜 발생했으며 관측 종료 기준은 무엇인가?
2. 장비별 차이를 계층모형으로 반영했는가?
3. 보수적인 RUL 하한과 정비 비용을 함께 고려했는가?