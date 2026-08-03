# 실습 393 — end_to_end_pipeline

## 1. 학습 목표
입력부터 결과 저장까지 전체 파이프라인을 실행합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
데이터 검증부터 특징 생성·결과 저장까지 전체 파이프라인을 실행하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage20
python examples\ex393_end_to_end_pipeline.py
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
| 17 | `def validate(df):` | 종합 프로젝트 통합 단계를 수행합니다. |
| 18 | `    required=["timestamp","equipment_id","yield_percent","fault_flag","rul_cycles"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    missing=[c for c in required if c not in df.columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    if missing:` | 종합 프로젝트 통합 단계를 수행합니다. |
| 21 | `        raise ValueError(missing)` | 종합 프로젝트 통합 단계를 수행합니다. |
| 22 | `    return df` | 종합 프로젝트 통합 단계를 수행합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `data=validate(pd.read_csv(DATA_FILE))` | 종합 프로젝트 데이터를 읽습니다. |
| 25 | `data["health_score"]=np.exp(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    -(.3*np.abs(data["temperature_c"]-72)+.25*np.abs(data["pressure_pa"]-18)+` | 종합 프로젝트 통합 단계를 수행합니다. |
| 27 | `      5*np.maximum(data["vibration_rms_g"]-.09,0)+.04*np.maximum(data["particle_count"]-8,0))` | 종합 프로젝트 통합 단계를 수행합니다. |
| 28 | `)` | 종합 프로젝트 통합 단계를 수행합니다. |
| 29 | `result=data[["timestamp","equipment_id","yield_percent","fault_flag","rul_cycles","health_score"]]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `result.to_csv(OUTPUT_DIR/"ex393_end_to_end_result.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |
| 31 | `print(result.head().round(4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 요구사항과 구현·평가 결과가 추적 가능한가?
2. 데이터 누수·안전·운영 실패 시나리오를 검토했는가?
3. 포트폴리오에서 문제·해결·성과를 수치로 설명할 수 있는가?