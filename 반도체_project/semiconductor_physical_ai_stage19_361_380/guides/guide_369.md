# 실습 369 — model_versioning

## 1. 학습 목표
모델과 메타데이터 버전을 저장합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
학습 모델과 버전 메타데이터를 joblib·JSON으로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex369_model_versioning.py
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
| 19 | `from datetime import datetime` | 필요한 라이브러리를 불러옵니다. |
| 20 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리를 불러옵니다. |
| 21 | `ops_df=pd.read_csv(DATA_FILE)` | 운영 센서 스트림 CSV를 읽습니다. |
| 22 | `features=["temperature_c","pressure_pa","vibration_rms_g","particle_count","cycle_time_min","yield_percent"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `model=RandomForestClassifier(n_estimators=300,class_weight="balanced",random_state=42,n_jobs=-1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `model.fit(ops_df[features],ops_df["fault_flag"])` | 운영 데이터로 모델을 학습합니다. |
| 25 | `version=datetime.now().strftime("%Y%m%d_%H%M%S")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `model_file=MODEL_DIR/f"fault_model_{version}.joblib"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `meta_file=MODEL_DIR/f"fault_model_{version}.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `joblib.dump(model,model_file)` | 학습 모델을 파일로 저장합니다. |
| 29 | `meta={"version":version,"features":features,"rows":len(ops_df),"model_type":"RandomForestClassifier"}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `meta_file.write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `print("모델:",model_file)` | 결과를 콘솔에 출력합니다. |
| 32 | `print("메타데이터:",meta_file)` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?