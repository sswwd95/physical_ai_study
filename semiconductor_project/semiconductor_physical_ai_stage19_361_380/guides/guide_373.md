# 실습 373 — model_performance_monitor

## 1. 학습 목표
운영 정답이 있을 때 모델 성능을 집계합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
운영 정답 기준 accuracy·precision·recall·F1을 집계하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex373_model_performance_monitor.py
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
| 19 | `from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score` | 필요한 라이브러리를 불러옵니다. |
| 20 | `model_files=sorted(MODEL_DIR.glob("fault_model_*.joblib"))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `if not model_files:` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 22 | `    raise FileNotFoundError("먼저 실습 369를 실행하세요.")` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 23 | `model=joblib.load(model_files[-1])` | 저장된 모델을 다시 불러옵니다. |
| 24 | `ops_df=pd.read_csv(DATA_FILE)` | 운영 센서 스트림 CSV를 읽습니다. |
| 25 | `features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `pred=model.predict(ops_df[features])` | 모델 예측값을 계산합니다. |
| 27 | `metrics=pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    "accuracy":accuracy_score(ops_df["fault_flag"],pred),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 29 | `    "precision":precision_score(ops_df["fault_flag"],pred,zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    "recall":recall_score(ops_df["fault_flag"],pred,zero_division=0),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    "f1":f1_score(ops_df["fault_flag"],pred,zero_division=0)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `}])` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 33 | `print(metrics.round(4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?