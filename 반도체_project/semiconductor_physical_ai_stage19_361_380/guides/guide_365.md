# 실습 365 — batch_processing

## 1. 학습 목표
대용량 데이터를 배치 단위로 처리합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
설정 batch_size로 데이터를 나누고 배치별 수율·고장수를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex365_batch_processing.py
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
| 18 | `with CONFIG_FILE.open("r",encoding="utf-8") as f:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    config=json.load(f)` | JSON 설정 파일을 읽습니다. |
| 20 | `batch_size=int(config["batch_size"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `ops_df=pd.read_csv(DATA_FILE)` | 운영 센서 스트림 CSV를 읽습니다. |
| 22 | `rows=[]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `for start in range(0,len(ops_df),batch_size):` | 여러 파일·배치·장비를 반복 처리합니다. |
| 24 | `    batch=ops_df.iloc[start:start+batch_size]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    rows.append({` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 26 | `        "batch_no":len(rows)+1,` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 27 | `        "start_row":start,` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 28 | `        "end_row":start+len(batch)-1,` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 29 | `        "row_count":len(batch),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 30 | `        "mean_yield":batch["yield_percent"].mean(),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 31 | `        "fault_count":int(batch["fault_flag"].sum())` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 32 | `    })` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 33 | `out=pd.DataFrame(rows)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `print(out)` | 결과를 콘솔에 출력합니다. |
| 35 | `out.to_csv(OUTPUT_DIR/"ex365_batch_summary.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?