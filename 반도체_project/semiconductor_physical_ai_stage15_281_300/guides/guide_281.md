# 실습 281 — optimization_data_profile

## 1. 학습 목표
최적화 이력과 후보 공간을 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
공정 최적화 이력과 후보공간의 크기·범위를 요약하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage15
python examples\ex281_optimization_data_profile.py
```

## 4. 예상 결과
요청한 공정 최적화·베이지안 의사결정 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `HISTORY_FILE = ROOT / "data" / "process_optimization_history.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `CANDIDATE_FILE = ROOT / "data" / "optimization_candidates.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 11 | `history_df = pd.read_csv(HISTORY_FILE)` | 과거 공정 기록 또는 후보 조건 CSV를 읽습니다. |
| 12 | `candidate_df = pd.read_csv(CANDIDATE_FILE)` | 과거 공정 기록 또는 후보 조건 CSV를 읽습니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `print("이력 데이터:", history_df.shape)` | 결과를 콘솔에 출력합니다. |
| 15 | `print("후보 데이터:", candidate_df.shape)` | 결과를 콘솔에 출력합니다. |
| 16 | `print("레시피:", sorted(history_df["recipe"].unique()))` | 결과를 콘솔에 출력합니다. |
| 17 | `print("챔버:", sorted(history_df["chamber_id"].unique()))` | 결과를 콘솔에 출력합니다. |
| 18 | `print(history_df[["uniformity_percent","defect_rate","cycle_time_min"]].describe().round(4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 목적함수와 제약조건이 실제 품질·안전 기준을 반영하는가?
2. 추천 조건이 과거 운전 범위를 벗어나지 않는가?
3. 최적 조건을 바로 양산에 적용하지 않고 확인 실험을 거치는가?