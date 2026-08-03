# 실습 370 — model_loading_inference

## 1. 학습 목표
저장 모델을 로드해 추론합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
최신 모델을 로드해 고장 예측과 확률을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex370_model_loading_inference.py
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
| 18 | `import joblib` | 필요한 라이브러리를 불러옵니다. |
| 19 | `model_files=sorted(MODEL_DIR.glob("fault_model_*.joblib"))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `if not model_files:` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 21 | `    raise FileNotFoundError("먼저 실습 369를 실행하세요.")` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 22 | `latest=model_files[-1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `model=joblib.load(latest)` | 저장된 모델을 다시 불러옵니다. |
| 24 | `ops_df=pd.read_csv(DATA_FILE)` | 운영 센서 스트림 CSV를 읽습니다. |
| 25 | `features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `ops_df["predicted_fault"]=model.predict(ops_df[features])` | 모델 예측값을 계산합니다. |
| 27 | `ops_df["fault_probability"]=model.predict_proba(ops_df[features])[:,1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `print(ops_df[["predicted_fault","fault_probability"]].head())` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?