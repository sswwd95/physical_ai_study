# 실습 274 — optimal_condition_probability

## 1. 학습 목표
각 조건이 최고 품질일 확률을 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
각 레시피·압력·RF 조건이 최고 균일도일 확률을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex274_optimal_condition_probability.py
```

## 4. 예상 결과
요청한 베이지안 실험분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_process_experiment.csv"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 11 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 12 | `experiment_df = pd.read_csv(DATA_FILE)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `group=experiment_df.groupby(["recipe","pressure_level","rf_level"])["uniformity_percent"].agg(["mean","std","count"]).reset_index()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `mu=group["mean"].to_numpy(); se=(group["std"]/np.sqrt(group["count"])).fillna(.2).to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `draws=np.random.default_rng(42).normal(mu,se,size=(4000,len(group)))` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 17 | `winner=np.argmax(draws,axis=1)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 18 | `group["p_best"]=np.bincount(winner,minlength=len(group))/len(winner)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 19 | `out=group.sort_values("p_best",ascending=False)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 20 | `print(out.head(10).round(4))` | 결과를 콘솔에 출력합니다. |
| 21 | `out.to_csv(OUTPUT_DIR/"ex274_optimal_condition_probability.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?