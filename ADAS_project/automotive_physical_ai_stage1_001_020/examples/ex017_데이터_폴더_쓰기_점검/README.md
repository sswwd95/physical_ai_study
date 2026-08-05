# 예제 017 — 데이터 폴더 쓰기 점검

## 핵심 주제
CSV 로그 생성과 재읽기를 통해 권한·인코딩을 확인한다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex017_데이터_폴더_쓰기_점검\main.py
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
| 2 | `import pandas as pd` | 필요한 표준/외부 모듈을 불러옵니다. |
| 3 | `` | 가독성을 위한 빈 줄입니다. |
| 4 | `out = Path(__file__).resolve().parents[2] / "data"` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 5 | `out.mkdir(exist_ok=True)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 6 | `path = out / "environment_test.csv"` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 7 | `df = pd.DataFrame({"time_s": [0.0, 0.1, 0.2], "speed_mps": [0.0, 0.1, 0.2]})` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 8 | `df.to_csv(path, index=False, encoding="utf-8-sig")` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 9 | `print(pd.read_csv(path))` | 실행 결과나 진단 정보를 화면에 출력합니다. |
| 10 | `print("saved:", path)` | 실행 결과나 진단 정보를 화면에 출력합니다. |
