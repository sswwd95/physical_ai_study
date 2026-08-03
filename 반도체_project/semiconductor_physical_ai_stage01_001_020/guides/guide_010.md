# 실습 010 — detect_duplicate_rows

## 1. 학습 목표
중복 행을 찾아 제거하고 데이터 품질 점검 절차를 익힙니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
센서 데이터의 앞 3개 행을 복사해 중복 데이터를 만든 뒤 duplicated로 찾고
drop_duplicates로 제거하는 예제를 작성하라. 처리 전후 행 수를 출력하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex010_detect_duplicate_rows.py
```

## 4. 예상 결과
303행 중 중복 3행을 탐지하고 제거 후 다시 300행이 됩니다.

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
| 9 | `sensor_df = pd.read_csv(DATA_FILE)` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 10 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 11 | `duplicated_sample = sensor_df.iloc[:3].copy()` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 12 | `working_df = pd.concat([sensor_df, duplicated_sample], ignore_index=True)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 13 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 14 | `duplicate_count = working_df.duplicated().sum()` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 15 | `clean_df = working_df.drop_duplicates().reset_index(drop=True)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 17 | `print("처리 전 행 수:", len(working_df))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 18 | `print("중복 행 수:", duplicate_count)` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 19 | `print("처리 후 행 수:", len(clean_df))` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?