# 실습 364 — data_ingestion_pipeline

## 1. 학습 목표
입력 데이터 로딩과 기본 검증 파이프라인을 작성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
CSV 입력 로딩·필수컬럼·빈 데이터·시간정렬 검증 함수를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex364_data_ingestion_pipeline.py
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
| 18 | `def load_and_validate(path):` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 19 | `    df=pd.read_csv(path,parse_dates=["timestamp"])` | 운영 센서 스트림 CSV를 읽습니다. |
| 20 | `    required=["timestamp","equipment_id","temperature_c","pressure_pa","yield_percent","fault_flag"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    missing=[c for c in required if c not in df.columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    if missing:` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 23 | `        raise ValueError(f"필수 컬럼 누락: {missing}")` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 24 | `    if df.empty:` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 25 | `        raise ValueError("입력 데이터가 비어 있습니다.")` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 26 | `    return df.sort_values("timestamp").reset_index(drop=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 28 | `ops_df=load_and_validate(DATA_FILE)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `print(ops_df.head())` | 결과를 콘솔에 출력합니다. |
| 30 | `print("행 수:",len(ops_df))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?