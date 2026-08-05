# 예제 020 — 통합 스모크 테스트

## 핵심 주제
MuJoCo 센서 데이터를 만들고 PyMC로 평균 가속도를 추정한다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex020_통합_스모크_테스트\main.py
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
| 1 | `from pathlib import Path` | 필요한 표준/외부 모듈을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 표준/외부 모듈을 불러옵니다. |
| 3 | `import mujoco` | 필요한 표준/외부 모듈을 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 표준/외부 모듈을 불러옵니다. |
| 5 | `` | 가독성을 위한 빈 줄입니다. |
| 6 | `xml = Path(__file__).resolve().parents[2] / "common" / "minimal_car.xml"` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 7 | `model = mujoco.MjModel.from_xml_path(str(xml))` | MJCF XML 파일을 읽어 MuJoCo 모델로 컴파일합니다. |
| 8 | `data = mujoco.MjData(model)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 9 | `values = []` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 10 | `for _ in range(50):` | 여러 항목 또는 여러 시뮬레이션 스텝을 반복합니다. |
| 11 | `    mujoco.mj_step(model, data)` | 물리 시뮬레이션을 한 타임스텝 전진시킵니다. |
| 12 | `    values.append(float(data.sensordata[2]))` | 해당 기능을 실행하는 문장입니다. |
| 13 | `values = np.asarray(values)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 14 | `with pm.Model():` | PyMC 확률모형 컨텍스트를 시작합니다. |
| 15 | `    mu = pm.Normal("mu", mu=-9.81, sigma=2.0)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 16 | `    sigma = pm.HalfNormal("sigma", sigma=1.0)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 17 | `    pm.Normal("acc_z", mu=mu, sigma=sigma + 1e-6, observed=values)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 18 | `    idata = pm.sample(300, tune=300, chains=2, cores=1, random_seed=42, progressbar=False)` | MCMC 샘플링을 실행하여 사후분포를 계산합니다. |
| 19 | `print("samples:", len(values))` | 실행 결과나 진단 정보를 화면에 출력합니다. |
| 20 | `print("acc_z observed mean:", values.mean())` | 실행 결과나 진단 정보를 화면에 출력합니다. |
| 21 | `print("posterior mu mean:", float(idata.posterior["mu"].mean()))` | 실행 결과나 진단 정보를 화면에 출력합니다. |
| 22 | `print("INTEGRATED TEST PASS")` | 실행 결과나 진단 정보를 화면에 출력합니다. |
