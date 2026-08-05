# 예제 019 — 환경 보고서 생성

## 핵심 주제
설치 버전을 텍스트 보고서로 저장한다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex019_환경_보고서_생성\main.py
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
| 2 | `import platform, sys` | 필요한 표준/외부 모듈을 불러옵니다. |
| 3 | `import mujoco, pymc, numpy, pandas, arviz` | 필요한 표준/외부 모듈을 불러옵니다. |
| 4 | `` | 가독성을 위한 빈 줄입니다. |
| 5 | `lines = [` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 6 | `    f"OS={platform.platform()}", f"Python={sys.version}",` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 7 | `    f"MuJoCo={mujoco.__version__}", f"PyMC={pymc.__version__}",` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 8 | `    f"NumPy={numpy.__version__}", f"Pandas={pandas.__version__}", f"ArviZ={arviz.__version__}",` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 9 | `]` | 해당 기능을 실행하는 문장입니다. |
| 10 | `path = Path(__file__).resolve().parents[2] / "environment_report.txt"` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 11 | `path.write_text("\n".join(lines), encoding="utf-8")` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 12 | `print(path.read_text(encoding="utf-8"))` | 실행 결과나 진단 정보를 화면에 출력합니다. |
