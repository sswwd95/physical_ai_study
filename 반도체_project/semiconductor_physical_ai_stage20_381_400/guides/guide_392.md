# 실습 392 — safety_gate

## 1. 학습 목표
안전 게이트가 모델보다 우선하도록 검증합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
극한 센서 조건에서는 모델 판단보다 강제 안전정지를 우선하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex392_safety_gate.py
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
| 17 | `decision_file=OUTPUT_DIR/"ex391_decision_engine.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `if not decision_file.exists():` | 종합 프로젝트 통합 단계를 수행합니다. |
| 19 | `    raise FileNotFoundError("먼저 실습 391을 실행하세요.")` | 종합 프로젝트 통합 단계를 수행합니다. |
| 20 | `pred=pd.read_csv(decision_file)` | 종합 프로젝트 데이터를 읽습니다. |
| 21 | `data=pd.read_csv(DATA_FILE)` | 종합 프로젝트 데이터를 읽습니다. |
| 22 | `pred["safety_gate"]=np.where(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    (data["temperature_c"]>80)\|(data["pressure_pa"]>21)\|(data["vibration_rms_g"]>.18),` | 종합 프로젝트 통합 단계를 수행합니다. |
| 24 | `    "FORCED_SAFE_STOP",` | 종합 프로젝트 통합 단계를 수행합니다. |
| 25 | `    "MODEL_DECISION")` | 종합 프로젝트 통합 단계를 수행합니다. |
| 26 | `pred["final_action"]=np.where(pred["safety_gate"]=="FORCED_SAFE_STOP","FORCED_SAFE_STOP",pred["action"])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `print(pred["final_action"].value_counts())` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?