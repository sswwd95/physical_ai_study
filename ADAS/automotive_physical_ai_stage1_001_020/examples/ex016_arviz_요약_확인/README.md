# 예제 016 — ArviZ 요약 확인

## 핵심 주제
사후분포 요약표와 수렴 지표를 출력한다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex016_arviz_요약_확인\main.py
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
| 3 | `import arviz as az` | 필요한 표준/외부 모듈을 불러옵니다. |
| 4 | `` | 가독성을 위한 빈 줄입니다. |
| 5 | `y = np.array([0.48, 0.51, 0.50, 0.47, 0.53])` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 6 | `with pm.Model():` | PyMC 확률모형 컨텍스트를 시작합니다. |
| 7 | `    mu = pm.Normal("mu", 0.5, 0.1)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 8 | `    sigma = pm.HalfNormal("sigma", 0.1)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 9 | `    pm.Normal("y", mu, sigma, observed=y)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 10 | `    idata = pm.sample(400, tune=400, chains=2, cores=1, random_seed=7, progressbar=False)` | MCMC 샘플링을 실행하여 사후분포를 계산합니다. |
| 11 | `print(az.summary(idata, var_names=["mu", "sigma"]))` | 실행 결과나 진단 정보를 화면에 출력합니다. |
