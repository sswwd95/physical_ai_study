# 실습 263 — recipe_ab_defect_rate

## 1. 학습 목표
두 레시피의 불량률을 베타-이항 모형으로 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
ETCH-A와 ETCH-B 불량률을 베타-이항 A/B 테스트로 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex263_recipe_ab_defect_rate.py
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
| 14 | `group=experiment_df.loc[experiment_df["recipe"].isin(["ETCH-A","ETCH-B"])].groupby("recipe")[["wafer_count","defect_count"]].sum()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 16 | `    p_a=pm.Beta("p_a",1,1); p_b=pm.Beta("p_b",1,1)` | 0~1 범위의 불량률 사전분포를 정의합니다. |
| 17 | `    pm.Binomial("d_a",n=int(group.loc["ETCH-A","wafer_count"]),p=p_a,observed=int(group.loc["ETCH-A","defect_count"]))` | 웨이퍼 수와 불량 수를 이항분포로 연결합니다. |
| 18 | `    pm.Binomial("d_b",n=int(group.loc["ETCH-B","wafer_count"]),p=p_b,observed=int(group.loc["ETCH-B","defect_count"]))` | 웨이퍼 수와 불량 수를 이항분포로 연결합니다. |
| 19 | `    diff=pm.Deterministic("diff",p_b-p_a)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 20 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 21 | `s=idata.posterior["diff"].values.ravel()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 22 | `print("P(B defect rate > A):",round((s>0).mean(),4))` | 결과를 콘솔에 출력합니다. |
| 23 | `print("평균 차이:",round(s.mean(),5))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?