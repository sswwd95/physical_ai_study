# 실습 381 — project_charter

## 1. 학습 목표
종합 프로젝트 목표·범위·성과지표를 정의합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
종합 프로젝트의 문제·목표·범위·제외범위·성공지표를 JSON으로 정의하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex381_project_charter.py
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
| 17 | `charter={` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    "problem":"반도체 공정 수율 저하와 장비 고장 위험을 조기에 탐지",` | 종합 프로젝트 통합 단계를 수행합니다. |
| 19 | `    "objectives":[` | 종합 프로젝트 통합 단계를 수행합니다. |
| 20 | `        "수율 예측",` | 종합 프로젝트 통합 단계를 수행합니다. |
| 21 | `        "고장확률 예측",` | 종합 프로젝트 통합 단계를 수행합니다. |
| 22 | `        "RUL 예측",` | 종합 프로젝트 통합 단계를 수행합니다. |
| 23 | `        "운영 행동 추천",` | 종합 프로젝트 통합 단계를 수행합니다. |
| 24 | `        "안전 우선 의사결정"` | 종합 프로젝트 통합 단계를 수행합니다. |
| 25 | `    ],` | 종합 프로젝트 통합 단계를 수행합니다. |
| 26 | `    "scope":["데이터 검증","특징공학","모델링","평가","운영보고"],` | 종합 프로젝트 통합 단계를 수행합니다. |
| 27 | `    "out_of_scope":["실제 PLC 제어","실장비 자동정지"],` | 종합 프로젝트 통합 단계를 수행합니다. |
| 28 | `    "success_metrics":{` | 종합 프로젝트 통합 단계를 수행합니다. |
| 29 | `        "yield_mae_target":1.5,` | 종합 프로젝트 통합 단계를 수행합니다. |
| 30 | `        "fault_recall_target":0.80,` | 종합 프로젝트 통합 단계를 수행합니다. |
| 31 | `        "rul_mae_target":20.0` | 종합 프로젝트 통합 단계를 수행합니다. |
| 32 | `    }` | 종합 프로젝트 통합 단계를 수행합니다. |
| 33 | `}` | 종합 프로젝트 통합 단계를 수행합니다. |
| 34 | `file=PORTFOLIO_DIR/"project_charter.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `file.write_text(json.dumps(charter,ensure_ascii=False,indent=2),encoding="utf-8")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `print(file.read_text(encoding="utf-8"))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?