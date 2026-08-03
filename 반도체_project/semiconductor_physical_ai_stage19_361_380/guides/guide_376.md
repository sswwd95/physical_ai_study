# 실습 376 — equipment_health_summary

## 1. 학습 목표
장비별 건강 상태 요약을 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
장비별 수율·고장률·센서·건강등급 요약을 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex376_equipment_health_summary.py
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
| 18 | `ops_df=pd.read_csv(DATA_FILE)` | 운영 센서 스트림 CSV를 읽습니다. |
| 19 | `summary=ops_df.groupby("equipment_id").agg(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    mean_yield=("yield_percent","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    fault_rate=("fault_flag","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `    mean_temperature=("temperature_c","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    mean_vibration=("vibration_rms_g","mean"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    mean_cycle_time=("cycle_time_min","mean")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `)` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 26 | `summary["health_grade"]=pd.cut(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    summary["fault_rate"],` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 28 | `    [-np.inf,.01,.03,.06,np.inf],` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 29 | `    labels=["A","B","C","D"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `)` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 31 | `print(summary.round(4))` | 결과를 콘솔에 출력합니다. |
| 32 | `summary.to_csv(OUTPUT_DIR/"ex376_equipment_health.csv",encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?