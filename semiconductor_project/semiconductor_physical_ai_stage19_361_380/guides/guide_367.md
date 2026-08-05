# 실습 367 — feature_pipeline

## 1. 학습 목표
운영용 특징공학 파이프라인을 구성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
운영용 센서 편차·위험·건강점수 특징을 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex367_feature_pipeline.py
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
| 19 | `ops_df["thermal_deviation"]=(ops_df["temperature_c"]-72).abs()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `ops_df["pressure_deviation"]=(ops_df["pressure_pa"]-18).abs()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `ops_df["vibration_risk"]=(ops_df["vibration_rms_g"]-.09).clip(lower=0)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `ops_df["particle_risk"]=(ops_df["particle_count"]-8).clip(lower=0)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `ops_df["composite_health_score"]=np.exp(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    -(.35*ops_df["thermal_deviation"]+.30*ops_df["pressure_deviation"]+4*ops_df["vibration_risk"]+.05*ops_df["particle_risk"])` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 25 | `)` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 26 | `print(ops_df[["thermal_deviation","pressure_deviation","composite_health_score"]].describe().round(4))` | 결과를 콘솔에 출력합니다. |
| 27 | `ops_df.to_csv(OUTPUT_DIR/"ex367_feature_pipeline.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?