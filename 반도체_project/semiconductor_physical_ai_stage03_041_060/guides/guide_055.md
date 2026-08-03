# 실습 055 — lot_capability_comparison

## 1. 학습 목표
LOT별 Cp와 Cpk를 계산해 배치 간 공정능력을 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
lot_id별 챔버 온도 평균과 표준편차를 계산하고 LSL=69, USL=75를 사용하여
Cp, CPU, CPL, Cpk를 계산하라. Cpk가 낮은 순으로 정렬하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex055_lot_capability_comparison.py
```

## 4. 예상 결과
LOT별 Cp·Cpk가 계산되고 공정능력이 낮은 LOT부터 정렬됩니다.

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
| 17 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 18 | `lot_stats = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 19 | `    sensor_df.groupby("lot_id")["chamber_temp_c"]` | LOT 또는 소그룹 단위로 데이터를 묶습니다. |
| 20 | `    .agg(["mean", "std"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 21 | `    .reset_index()` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 22 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 24 | `lot_stats["cp"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 25 | `    (usl - lsl) / (6 * lot_stats["std"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 26 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 27 | `lot_stats["cpu"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 28 | `    (usl - lot_stats["mean"]) / (3 * lot_stats["std"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 29 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 30 | `lot_stats["cpl"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 31 | `    (lot_stats["mean"] - lsl) / (3 * lot_stats["std"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 32 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `lot_stats["cpk"] = lot_stats[["cpu", "cpl"]].min(axis=1)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 34 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 35 | `lot_stats = lot_stats.sort_values("cpk")` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 36 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 37 | `print(lot_stats.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 38 | `lot_stats.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 39 | `    OUTPUT_DIR / "ex055_lot_capability.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 40 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 41 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 42 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?