# 실습 374 — retry_and_recovery

## 1. 학습 목표
실패 작업 재시도와 체크포인트 복구를 구현합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
최대 3회 재시도와 JSON 체크포인트 복구를 구현하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex374_retry_and_recovery.py
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
| 18 | `checkpoint=OUTPUT_DIR/"ex374_checkpoint.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `max_retries=3` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `attempt=0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `completed=False` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `while attempt<max_retries and not completed:` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 23 | `    attempt+=1` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    try:` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 25 | `        ops_df=pd.read_csv(DATA_FILE)` | 운영 센서 스트림 CSV를 읽습니다. |
| 26 | `        if len(ops_df)==0:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `            raise ValueError("빈 데이터")` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 28 | `        completed=True` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `        checkpoint.write_text(json.dumps({"attempt":attempt,"status":"completed","rows":len(ops_df)},ensure_ascii=False,indent=2),encoding="utf-8")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    except Exception as e:` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 31 | `        checkpoint.write_text(json.dumps({"attempt":attempt,"status":"failed","error":str(e)},ensure_ascii=False,indent=2),encoding="utf-8")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `if not completed:` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 33 | `    raise RuntimeError("최대 재시도 횟수 초과")` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 34 | `print(checkpoint.read_text(encoding="utf-8"))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?