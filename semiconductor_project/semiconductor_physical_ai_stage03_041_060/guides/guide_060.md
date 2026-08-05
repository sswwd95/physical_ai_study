# 실습 060 — automated_spc_report

## 1. 학습 목표
공정 요약, 관리한계, 공정능력, 경보 건수를 하나의 Excel 보고서로 자동 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도와 압력에 대해 평균, 표준편차, UCL, LCL, 규격하한, 규격상한,
Cp, Cpk, 관리한계 이탈 수, 규격 이탈 수를 계산하라.
summary, alarm_rows 두 시트의 Excel 보고서를 생성하고 CSV 요약도 함께 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex060_automated_spc_report.py
```

## 4. 예상 결과
SPC 요약과 경보 행이 포함된 Excel 및 CSV 보고서가 생성됩니다.

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
| 13 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 15 | `specs = {` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `    "chamber_temp_c": {"lsl": 69.0, "usl": 75.0},` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 17 | `    "chamber_pressure_pa": {"lsl": 17.0, "usl": 19.0},` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 18 | `}` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 19 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 20 | `summary_rows = []` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `alarm_masks = []` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 23 | `for column, spec in specs.items():` | 여러 센서나 구간에 같은 작업을 반복합니다. |
| 24 | `    mean_value = sensor_df[column].mean()` | 데이터의 평균을 계산합니다. |
| 25 | `    std_value = sensor_df[column].std(ddof=1)` | 데이터의 표준편차를 계산합니다. |
| 26 | `    ucl = mean_value + 3 * std_value` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 27 | `    lcl = mean_value - 3 * std_value` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 28 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 29 | `    cp = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `        (spec["usl"] - spec["lsl"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 31 | `        / (6 * std_value)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 32 | `    )` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `    cpu = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 34 | `        (spec["usl"] - mean_value)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 35 | `        / (3 * std_value)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 36 | `    )` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 37 | `    cpl = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 38 | `        (mean_value - spec["lsl"])` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 39 | `        / (3 * std_value)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 40 | `    )` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 41 | `    cpk = min(cpu, cpl)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 42 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 43 | `    control_mask = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 44 | `        (sensor_df[column] > ucl)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 45 | `        \| (sensor_df[column] < lcl)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 46 | `    )` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 47 | `    spec_mask = ~sensor_df[column].between(` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 48 | `        spec["lsl"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 49 | `        spec["usl"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 50 | `    )` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 51 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 52 | `    summary_rows.append({` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 53 | `        "sensor": column,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 54 | `        "mean": mean_value,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 55 | `        "std": std_value,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 56 | `        "lcl": lcl,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 57 | `        "ucl": ucl,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 58 | `        "lsl": spec["lsl"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 59 | `        "usl": spec["usl"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 60 | `        "cp": cp,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 61 | `        "cpk": cpk,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 62 | `        "control_violation_count": int(control_mask.sum()),` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 63 | `        "spec_violation_count": int(spec_mask.sum()),` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 64 | `    })` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 65 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 66 | `    alarm_masks.append(control_mask \| spec_mask)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 67 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 68 | `summary_df = pd.DataFrame(summary_rows)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 69 | `combined_alarm = np.logical_or.reduce(alarm_masks)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 70 | `alarm_df = sensor_df.loc[combined_alarm]` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 71 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 72 | `excel_file = OUTPUT_DIR / "ex060_automated_spc_report.xlsx"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 73 | `with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 74 | `    summary_df.to_excel(` | 결과를 Excel 파일로 저장합니다. |
| 75 | `        writer,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 76 | `        sheet_name="summary",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 77 | `        index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 78 | `    )` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 79 | `    alarm_df.to_excel(` | 결과를 Excel 파일로 저장합니다. |
| 80 | `        writer,` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 81 | `        sheet_name="alarm_rows",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 82 | `        index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 83 | `    )` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 84 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 85 | `summary_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 86 | `    OUTPUT_DIR / "ex060_spc_summary.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 87 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 88 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 89 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 90 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 91 | `print(summary_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 92 | `print("Excel 보고서:", excel_file)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?