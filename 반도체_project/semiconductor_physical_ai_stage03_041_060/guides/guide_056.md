# 실습 056 — spec_violation_rate

## 1. 학습 목표
규격 이탈률을 계산해 실제 불량 후보 비율을 정량화합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 규격 69~75°C, 압력 규격 17~19Pa를 적용하라.
각 센서별 규격 이탈 건수와 이탈률, 둘 중 하나라도 이탈한 행 비율을 계산하여 출력하고
요약 CSV를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex056_spec_violation_rate.py
```

## 4. 예상 결과
센서별 규격 이탈 건수와 전체 이탈률이 계산됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 9 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 12 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE)` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 15 | `temp_violation = ~sensor_df["chamber_temp_c"].between(69, 75)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `pressure_violation = ~sensor_df["chamber_pressure_pa"].between(17, 19)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 17 | `any_violation = temp_violation \| pressure_violation` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 18 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 19 | `summary_df = pd.DataFrame([` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 20 | `    {` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 21 | `        "rule": "temperature",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 22 | `        "violation_count": int(temp_violation.sum()),` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `        "violation_rate": float(temp_violation.mean()),` | 데이터의 평균을 계산합니다. |
| 24 | `    },` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 25 | `    {` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 26 | `        "rule": "pressure",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 27 | `        "violation_count": int(pressure_violation.sum()),` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 28 | `        "violation_rate": float(pressure_violation.mean()),` | 데이터의 평균을 계산합니다. |
| 29 | `    },` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 30 | `    {` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 31 | `        "rule": "any",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 32 | `        "violation_count": int(any_violation.sum()),` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `        "violation_rate": float(any_violation.mean()),` | 데이터의 평균을 계산합니다. |
| 34 | `    },` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 35 | `])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 36 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 37 | `print(summary_df)` | 실행 결과를 콘솔에 출력합니다. |
| 38 | `summary_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 39 | `    OUTPUT_DIR / "ex056_spec_violation_rate.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 40 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 41 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 42 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?