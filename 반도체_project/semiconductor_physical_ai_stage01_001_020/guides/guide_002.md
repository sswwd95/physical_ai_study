# 실습 002 — load_and_inspect

## 1. 학습 목표
CSV를 읽고 행·열 개수, 컬럼명, 자료형, 앞부분 데이터를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
반도체 센서 CSV를 pandas로 읽고 shape, columns, dtypes, head를 출력하는
초보자용 점검 스크립트를 작성하라. 파일이 없으면 실습 001을 먼저 실행하라는
친절한 오류 메시지를 표시하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex002_load_and_inspect.py
```

## 4. 예상 결과
`(300, 9)` 형태의 크기, 9개 컬럼, 각 컬럼의 자료형과 처음 5행이 출력됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 실습에 필요한 외부 기능을 불러옵니다. |
| 2 | `import pandas as pd` | 실습에 필요한 외부 기능을 불러옵니다. |
| 3 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 4 | `ROOT = Path(__file__).resolve().parents[1]` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 5 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 6 | `OUTPUT_DIR = ROOT / "outputs"` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 7 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 8 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 9 | `if not DATA_FILE.exists():` | 실습 흐름에 필요한 명령을 수행합니다. |
| 10 | `    raise FileNotFoundError("데이터가 없습니다. 실습 001을 먼저 실행하세요.")` | 실습 흐름에 필요한 명령을 수행합니다. |
| 11 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 12 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 13 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 14 | `print("행과 열:", sensor_df.shape)` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 15 | `print("\n컬럼 목록:")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 16 | `print(sensor_df.columns.tolist())` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 17 | `print("\n자료형:")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 18 | `print(sensor_df.dtypes)` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 19 | `print("\n앞의 5행:")` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 20 | `print(sensor_df.head())` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?