# 실습 400 — final_project_package

## 1. 학습 목표
최종 종합 Excel·문서·manifest를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
일별KPI·장비요약·위험행동·품질검사 Excel과 최종 manifest를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex400_final_project_package.py
```

## 4. 예상 결과
요청한 종합 프로젝트·포트폴리오 산출물이 생성됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import json` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 5 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 6 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `DATA_FILE = ROOT / "data" / "final_project_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `CONFIG_FILE = ROOT / "config" / "project_config.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `MODEL_DIR = ROOT / "models"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 11 | `REPORT_DIR = ROOT / "reports"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 12 | `PORTFOLIO_DIR = ROOT / "portfolio"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `for directory in [OUTPUT_DIR, MODEL_DIR, REPORT_DIR, PORTFOLIO_DIR]:` | 여러 모델·지표·장비를 반복 처리합니다. |
| 15 | `    directory.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `data=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])` | 종합 프로젝트 데이터를 읽습니다. |
| 18 | `daily=data.assign(date=data["timestamp"].dt.date).groupby("date").agg(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    mean_yield=("yield_percent","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    fault_count=("fault_flag","sum"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    mean_rul=("rul_cycles","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    mean_cycle_time=("cycle_time_min","mean")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `)` | 종합 프로젝트 통합 단계를 수행합니다. |
| 24 | `equipment=data.groupby("equipment_id").agg(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    mean_yield=("yield_percent","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    fault_rate=("fault_flag","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    mean_rul=("rul_cycles","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    mean_temperature=("temperature_c","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    mean_vibration=("vibration_rms_g","mean")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `)` | 종합 프로젝트 통합 단계를 수행합니다. |
| 31 | `risk=data.loc[(data["fault_flag"]==1)\|(data["yield_percent"]<93)\|(data["rul_cycles"]<30)].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `risk["recommended_action"]=np.select(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    [risk["fault_flag"]==1,risk["rul_cycles"]<15,risk["yield_percent"]<90],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    ["INSPECT_NOW","MAINTENANCE_SOON","PROCESS_HOLD"],` | 종합 프로젝트 통합 단계를 수행합니다. |
| 35 | `    default="MONITOR")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `quality=pd.DataFrame([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `    {"check":"missing","failed":int(data.isna().sum().sum())},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 38 | `    {"check":"duplicates","failed":int(data.duplicated().sum())},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 39 | `    {"check":"yield_range","failed":int((~data["yield_percent"].between(0,100)).sum())}` | 종합 프로젝트 통합 단계를 수행합니다. |
| 40 | `])` | 종합 프로젝트 통합 단계를 수행합니다. |
| 41 | `excel=REPORT_DIR/"final_project_report.xlsx"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `with pd.ExcelWriter(excel,engine="openpyxl") as w:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    daily.to_excel(w,sheet_name="daily_kpi")` | 결과를 Excel로 저장합니다. |
| 44 | `    equipment.to_excel(w,sheet_name="equipment_summary")` | 결과를 Excel로 저장합니다. |
| 45 | `    risk.to_excel(w,sheet_name="risk_actions",index=False)` | 결과를 Excel로 저장합니다. |
| 46 | `    quality.to_excel(w,sheet_name="data_quality",index=False)` | 결과를 Excel로 저장합니다. |
| 47 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 48 | `manifest={` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `    "project":"Semiconductor Physical AI Final Project",` | 종합 프로젝트 통합 단계를 수행합니다. |
| 50 | `    "examples":20,` | 종합 프로젝트 통합 단계를 수행합니다. |
| 51 | `    "data_rows":len(data),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 52 | `    "report_file":excel.name,` | 종합 프로젝트 통합 단계를 수행합니다. |
| 53 | `    "portfolio_files":[p.name for p in PORTFOLIO_DIR.glob("*")],` | 종합 프로젝트 통합 단계를 수행합니다. |
| 54 | `    "generated_outputs":[p.name for p in OUTPUT_DIR.glob("*")]` | 종합 프로젝트 통합 단계를 수행합니다. |
| 55 | `}` | 종합 프로젝트 통합 단계를 수행합니다. |
| 56 | `manifest_file=REPORT_DIR/"final_project_manifest.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `manifest_file.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `print("최종 보고서:",excel)` | 결과를 콘솔에 출력합니다. |
| 59 | `print("Manifest:",manifest_file)` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?