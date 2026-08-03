# 실습 399 — deployment_checklist

## 1. 학습 목표
배포·운영·안전 체크리스트를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
환경·데이터·모델·안전·모니터링·복구·문서 체크리스트를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex399_deployment_checklist.py
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
| 17 | `items=[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    ("환경 재현","environment.yml 검증"),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 19 | `    ("데이터 계약","컬럼·범위·결측 규칙 검증"),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 20 | `    ("모델 버전","모델 파일·메타데이터 확인"),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 21 | `    ("평가 기준","KPI 목표 통과 확인"),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 22 | `    ("안전 게이트","모델보다 인터록 우선 확인"),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 23 | `    ("모니터링","드리프트·성능·경보 확인"),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 24 | `    ("복구","로그·체크포인트·재실행 절차 확인"),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 25 | `    ("문서","README·운영가이드·포트폴리오 확인")` | 종합 프로젝트 통합 단계를 수행합니다. |
| 26 | `]` | 종합 프로젝트 통합 단계를 수행합니다. |
| 27 | `check=pd.DataFrame(items,columns=["area","check_item"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `check["status"]="TO_REVIEW"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `print(check)` | 결과를 콘솔에 출력합니다. |
| 30 | `check.to_csv(PORTFOLIO_DIR/"deployment_checklist.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?