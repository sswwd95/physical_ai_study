# 실습 380 — automated_operations_report

## 1. 학습 목표
자동 운영 통합 Excel 보고서를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
일별KPI·장비건강·경보·데이터품질 Excel 보고서를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex380_automated_operations_report.py
```

## 4. 예상 결과
요청한 시스템 통합·운영 자동화 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import json` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import logging` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "operations_stream.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `CONFIG_FILE = ROOT / "config" / "app_config.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 11 | `LOG_DIR = ROOT / "logs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 12 | `MODEL_DIR = ROOT / "models"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 13 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 14 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 15 | `LOG_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `MODEL_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 18 | `ops_df=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])` | 운영 센서 스트림 CSV를 읽습니다. |
| 19 | `ops_df["date"]=ops_df["timestamp"].dt.date` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `daily=ops_df.groupby("date").agg(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    mean_yield=("yield_percent","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    fault_count=("fault_flag","sum"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    mean_cycle_time=("cycle_time_min","mean")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `)` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 25 | `equipment=ops_df.groupby("equipment_id").agg(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    mean_yield=("yield_percent","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    fault_rate=("fault_flag","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    mean_temperature=("temperature_c","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    mean_vibration=("vibration_rms_g","mean")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `)` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 31 | `alerts=ops_df.loc[(ops_df["fault_flag"]==1)\|(ops_df["yield_percent"]<93)].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `alerts["alert_type"]=np.where(alerts["fault_flag"]==1,"FAULT_RISK","LOW_YIELD")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `quality=pd.DataFrame([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    {"check":"missing_values","failed":int(ops_df.isna().sum().sum())},` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 35 | `    {"check":"duplicates","failed":int(ops_df.duplicated().sum())},` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 36 | `    {"check":"yield_out_of_range","failed":int((~ops_df["yield_percent"].between(0,100)).sum())}` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 37 | `])` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 38 | `with pd.ExcelWriter(OUTPUT_DIR/"ex380_operations_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `    daily.to_excel(w,sheet_name="daily_kpi")` | 결과를 Excel 보고서로 저장합니다. |
| 40 | `    equipment.to_excel(w,sheet_name="equipment_health")` | 결과를 Excel 보고서로 저장합니다. |
| 41 | `    alerts.to_excel(w,sheet_name="alerts",index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 42 | `    quality.to_excel(w,sheet_name="data_quality",index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 43 | `print("보고서 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?