# 예제 014 — PyMC 동전 확률 추정

## 핵심 주제
가장 작은 베이지안 모델로 샘플링 동작을 검증한다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex014_pymc_동전_확률_추정\main.py
```

## 기대 결과
오류 없이 진단 정보 또는 계산 결과가 출력됩니다. 외부 모델이 필요한 예제는 모델 경로가 없을 때 안전하게 `SKIP` 또는 안내 문구를 출력합니다.

## 초보자 체크포인트
- `python` 실행 경로가 `auto_physical_ai` 환경인지 확인합니다.
- 패키지 오류가 나면 `conda env update -f environment.yml --prune`을 실행합니다.
- 경로 문제를 줄이기 위해 압축 해제 위치에 한글과 공백을 사용하지 않는 것을 권장합니다.

## 라인별 해설
| 줄 | 코드 | 설명 |
|---:|---|---|
| 1 | `import numpy as np` | 필요한 표준/외부 모듈을 불러옵니다. |
| 2 | `import pymc as pm` | 필요한 표준/외부 모듈을 불러옵니다. |
| 3 | `` | 가독성을 위한 빈 줄입니다. |
| 4 | `observed = np.array([1, 1, 0, 1, 0, 1, 1, 1, 0, 1])` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 5 | `with pm.Model() as model:` | PyMC 확률모형 컨텍스트를 시작합니다. |
| 6 | `    theta = pm.Beta("theta", alpha=1, beta=1)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 7 | `    pm.Bernoulli("obs", p=theta, observed=observed)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 8 | `    idata = pm.sample(500, tune=500, chains=2, cores=1, random_seed=42, progressbar=False)` | MCMC 샘플링을 실행하여 사후분포를 계산합니다. |
| 9 | `print("posterior mean:", float(idata.posterior["theta"].mean()))` | 실행 결과나 진단 정보를 화면에 출력합니다. |
