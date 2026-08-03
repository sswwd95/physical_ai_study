# 실습 275 — multiobjective_utility

## 1. 학습 목표
균일도·불량률·식각률을 결합한 효용을 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
균일도·불량률·식각률을 결합한 다목적 효용을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex275_multiobjective_utility.py
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
| 14 | `group=experiment_df.groupby(["recipe","pressure_level","rf_level"])[` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `    ["uniformity_percent","defect_rate","etch_rate_nm_min"]` | 베이지안 실험분석 단계를 수행합니다. |
| 16 | `].mean().reset_index()` | 베이지안 실험분석 단계를 수행합니다. |
| 17 | `group["utility"]=(` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 18 | `    0.5*(group["uniformity_percent"]-group["uniformity_percent"].mean())/group["uniformity_percent"].std()` | 베이지안 실험분석 단계를 수행합니다. |
| 19 | `    -0.35*(group["defect_rate"]-group["defect_rate"].mean())/group["defect_rate"].std()` | 베이지안 실험분석 단계를 수행합니다. |
| 20 | `    +0.15*(group["etch_rate_nm_min"]-group["etch_rate_nm_min"].mean())/group["etch_rate_nm_min"].std()` | 베이지안 실험분석 단계를 수행합니다. |
| 21 | `)` | 베이지안 실험분석 단계를 수행합니다. |
| 22 | `out=group.sort_values("utility",ascending=False)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 23 | `print(out.head(10).round(4))` | 결과를 콘솔에 출력합니다. |
| 24 | `out.to_csv(OUTPUT_DIR/"ex275_multiobjective_utility.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?