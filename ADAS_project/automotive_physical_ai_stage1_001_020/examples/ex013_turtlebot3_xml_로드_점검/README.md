# 예제 013 — TurtleBot3 XML 로드 점검

## 핵심 주제
찾은 robotis_tb3 XML을 MuJoCo로 컴파일한다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex013_turtlebot3_xml_로드_점검\main.py
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
| 1 | `import sys` | 필요한 표준/외부 모듈을 불러옵니다. |
| 2 | `from pathlib import Path` | 필요한 표준/외부 모듈을 불러옵니다. |
| 3 | `import mujoco` | 필요한 표준/외부 모듈을 불러옵니다. |
| 4 | `` | 가독성을 위한 빈 줄입니다. |
| 5 | `sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "common"))` | 해당 기능을 실행하는 문장입니다. |
| 6 | `from locate_tb3_model import find_tb3_model` | 필요한 표준/외부 모듈을 불러옵니다. |
| 7 | `` | 가독성을 위한 빈 줄입니다. |
| 8 | `path = find_tb3_model()` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 9 | `if path is None:` | 조건에 따라 실행 흐름을 나눕니다. |
| 10 | `    print("SKIP: robotis_tb3 모델 경로 미설정")` | 실행 결과나 진단 정보를 화면에 출력합니다. |
| 11 | `else:` | 해당 기능을 실행하는 문장입니다. |
| 12 | `    model = mujoco.MjModel.from_xml_path(str(path))` | MJCF XML 파일을 읽어 MuJoCo 모델로 컴파일합니다. |
| 13 | `    print("loaded:", path)` | 실행 결과나 진단 정보를 화면에 출력합니다. |
| 14 | `    print("nbody/njnt/nu/nsensor:", model.nbody, model.njnt, model.nu, model.nsensor)` | 실행 결과나 진단 정보를 화면에 출력합니다. |
