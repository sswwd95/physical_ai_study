# 실습 379 — operations_checklist

## 1. 학습 목표
운영 점검 체크리스트를 자동 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
운영 전 필수 점검 체크리스트를 CSV로 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex379_operations_checklist.py
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
| 18 | `checks=[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    ("입력 데이터 존재",DATA_FILE.exists()),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 20 | `    ("설정 파일 존재",CONFIG_FILE.exists()),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 21 | `    ("출력 폴더 존재",OUTPUT_DIR.exists()),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 22 | `    ("로그 폴더 존재",LOG_DIR.exists()),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 23 | `    ("모델 폴더 존재",MODEL_DIR.exists()),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 24 | `    ("데이터 행 수 1 이상",len(pd.read_csv(DATA_FILE))>0),` | 운영 센서 스트림 CSV를 읽습니다. |
| 25 | `    ("운영 로그 생성 가능",LOG_DIR.is_dir()),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 26 | `]` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 27 | `check_df=pd.DataFrame(checks,columns=["check_item","passed"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `check_df["status"]=np.where(check_df["passed"],"OK","ACTION_REQUIRED")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `print(check_df)` | 결과를 콘솔에 출력합니다. |
| 30 | `check_df.to_csv(OUTPUT_DIR/"ex379_operations_checklist.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?