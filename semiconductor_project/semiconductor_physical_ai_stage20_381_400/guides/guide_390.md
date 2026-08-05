# 실습 390 — integrated_inference

## 1. 학습 목표
수율·고장확률·RUL 통합 추론을 수행합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
등록된 세 모델을 로드해 통합 예측 CSV를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex390_integrated_inference.py
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
| 17 | `import joblib` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `registry_file=MODEL_DIR/"model_registry.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `if not registry_file.exists():` | 종합 프로젝트 통합 단계를 수행합니다. |
| 20 | `    raise FileNotFoundError("먼저 실습 389를 실행하세요.")` | 종합 프로젝트 통합 단계를 수행합니다. |
| 21 | `registry=json.loads(registry_file.read_text(encoding="utf-8"))` | 프로젝트 설정 파일을 읽습니다. |
| 22 | `data=pd.read_csv(DATA_FILE)` | 종합 프로젝트 데이터를 읽습니다. |
| 23 | `features=registry[0]["features"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `models={item["name"]:joblib.load(MODEL_DIR/item["file"]) for item in registry}` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `out=data[["timestamp","equipment_id","recipe","chamber_id"]].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `out["predicted_yield"]=models["yield"].predict(data[features])` | 수율·고장·RUL 예측값을 계산합니다. |
| 27 | `out["fault_probability"]=models["fault"].predict_proba(data[features])[:,1]` | 고장 위험확률을 계산합니다. |
| 28 | `out["predicted_rul"]=models["rul"].predict(data[features])` | 수율·고장·RUL 예측값을 계산합니다. |
| 29 | `print(out.head().round(4))` | 결과를 콘솔에 출력합니다. |
| 30 | `out.to_csv(OUTPUT_DIR/"ex390_integrated_inference.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?