# 실습 382 — requirements_traceability

## 1. 학습 목표
요구사항과 구현·검증 항목을 연결합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
요구사항 ID와 구현 실습·검증 지표를 연결한 추적표를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex382_requirements_traceability.py
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
| 17 | `requirements=[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    {"id":"REQ-01","requirement":"수율 예측","implementation":"ex386","verification":"MAE/R2"},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 19 | `    {"id":"REQ-02","requirement":"고장 확률","implementation":"ex387","verification":"Recall/F1"},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 20 | `    {"id":"REQ-03","requirement":"RUL 예측","implementation":"ex388","verification":"MAE/R2"},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 21 | `    {"id":"REQ-04","requirement":"통합 추론","implementation":"ex390","verification":"output schema"},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 22 | `    {"id":"REQ-05","requirement":"안전 우선","implementation":"ex392","verification":"safety gate tests"},` | 종합 프로젝트 통합 단계를 수행합니다. |
| 23 | `    {"id":"REQ-06","requirement":"운영 보고서","implementation":"ex400","verification":"Excel sheets"}` | 종합 프로젝트 통합 단계를 수행합니다. |
| 24 | `]` | 종합 프로젝트 통합 단계를 수행합니다. |
| 25 | `df_req=pd.DataFrame(requirements)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `print(df_req)` | 결과를 콘솔에 출력합니다. |
| 27 | `df_req.to_csv(REPORT_DIR/"requirements_traceability.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?