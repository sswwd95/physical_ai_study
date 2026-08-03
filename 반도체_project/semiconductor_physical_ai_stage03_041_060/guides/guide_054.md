# 실습 054 — cpk_calculation

## 1. 학습 목표
공정 평균의 치우침까지 반영하는 Cpk를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
챔버 온도의 LSL=69, USL=75를 사용하라.
CPU=(USL-mean)/(3*sigma), CPL=(mean-LSL)/(3*sigma), Cpk=min(CPU,CPL)를 계산하고
평균이 어느 규격 쪽에 더 가까운지 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex054_cpk_calculation.py
```

## 4. 예상 결과
상·하한 방향 능력과 최종 Cpk가 출력됩니다.

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
| 15 | `lsl = 69.0` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `usl = 75.0` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 17 | `mean_value = sensor_df["chamber_temp_c"].mean()` | 데이터의 평균을 계산합니다. |
| 18 | `sigma = sensor_df["chamber_temp_c"].std(ddof=1)` | 데이터의 표준편차를 계산합니다. |
| 19 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 20 | `cpu = (usl - mean_value) / (3 * sigma)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `cpl = (mean_value - lsl) / (3 * sigma)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `cpk = min(cpu, cpl)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 24 | `near_side = "USL" if cpu < cpl else "LSL"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 25 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 26 | `print(f"평균={mean_value:.4f}, 표준편차={sigma:.4f}")` | 실행 결과를 콘솔에 출력합니다. |
| 27 | `print(f"CPU={cpu:.4f}, CPL={cpl:.4f}, Cpk={cpk:.4f}")` | 실행 결과를 콘솔에 출력합니다. |
| 28 | `print("평균이 더 가까운 규격:", near_side)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?