# 실습 371 — prediction_monitoring

## 1. 학습 목표
예측 분포와 임계값 초과 건수를 모니터링합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
예측확률 평균·95분위·0.7·0.9 초과 건수를 집계하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex371_prediction_monitoring.py
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
| 22 | `model=joblib.load(model_files[-1])` | 저장된 모델을 다시 불러옵니다. |
| 23 | `ops_df=pd.read_csv(DATA_FILE)` | 운영 센서 스트림 CSV를 읽습니다. |
| 24 | `features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `prob=model.predict_proba(ops_df[features])[:,1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `summary=pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    "prediction_count":len(prob),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 28 | `    "mean_probability":prob.mean(),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 29 | `    "p95_probability":np.quantile(prob,.95),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 30 | `    "above_070":int((prob>=.70).sum()),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    "above_090":int((prob>=.90).sum())` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `}])` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 33 | `print(summary.round(4))` | 결과를 콘솔에 출력합니다. |
| 34 | `summary.to_csv(OUTPUT_DIR/"ex371_prediction_monitoring.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?