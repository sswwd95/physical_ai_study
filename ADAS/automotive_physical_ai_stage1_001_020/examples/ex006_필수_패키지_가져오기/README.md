# 예제 006 — 필수 패키지 가져오기

## 핵심 주제
핵심 패키지를 import하고 버전을 표로 출력한다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex006_필수_패키지_가져오기\main.py
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
| 1 | `import importlib` | 필요한 표준/외부 모듈을 불러옵니다. |
| 2 | `` | 가독성을 위한 빈 줄입니다. |
| 3 | `packages = ["numpy", "pandas", "matplotlib", "mujoco", "pymc", "arviz"]` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 4 | `for name in packages:` | 여러 항목 또는 여러 시뮬레이션 스텝을 반복합니다. |
| 5 | `    module = importlib.import_module(name)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 6 | `    print(f"{name:12s} {getattr(module, '__version__', 'unknown')}")` | 실행 결과나 진단 정보를 화면에 출력합니다. |
