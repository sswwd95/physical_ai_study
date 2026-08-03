# 실습 363 — structured_logging

## 1. 학습 목표
파일·콘솔 구조화 로그를 구성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
콘솔과 파일에 동시에 기록하는 구조화 로그를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex363_structured_logging.py
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
| 18 | `log_file=LOG_DIR/"stage19_operations.log"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `logging.basicConfig(` | 운영 로그 설정 또는 기록을 수행합니다. |
| 20 | `    level=logging.INFO,` | 운영 로그 설정 또는 기록을 수행합니다. |
| 21 | `    format="%(asctime)s \| %(levelname)s \| %(message)s",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    handlers=[logging.FileHandler(log_file,encoding="utf-8"),logging.StreamHandler()]` | 운영 로그 설정 또는 기록을 수행합니다. |
| 23 | `)` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 24 | `logging.info("운영 자동화 시작")` | 운영 로그 설정 또는 기록을 수행합니다. |
| 25 | `ops_df=pd.read_csv(DATA_FILE)` | 운영 센서 스트림 CSV를 읽습니다. |
| 26 | `logging.info("데이터 로드 완료: %d행",len(ops_df))` | 운영 로그 설정 또는 기록을 수행합니다. |
| 27 | `logging.info("운영 자동화 정상 종료")` | 운영 로그 설정 또는 기록을 수행합니다. |
| 28 | `print("로그 파일:",log_file)` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?