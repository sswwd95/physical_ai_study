# 실습 221 — maintenance_data_profile

## 1. 학습 목표
장비별 수명과 센서 열화 분포를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
장비별 수명, 고장 수, 정상·고장 센서 평균을 요약하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage12
python examples\ex221_maintenance_data_profile.py
```

## 4. 예상 결과
요청한 예지보전 분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "predictive_maintenance_rul.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 예지보전 분석 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 예지보전 분석 단계를 수행합니다. |
| 12 | `        "data/predictive_maintenance_rul.csv 파일이 없습니다."` | 예지보전 분석 단계를 수행합니다. |
| 13 | `    )` | 예지보전 분석 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `pm_df = pd.read_csv(DATA_FILE)` | 예지보전용 CSV를 DataFrame으로 읽습니다. |
| 16 | `print("데이터 크기:", pm_df.shape)` | 결과를 콘솔에 출력합니다. |
| 17 | `print("장비 수:", pm_df["equipment_id"].nunique())` | 결과를 콘솔에 출력합니다. |
| 18 | `life_summary = pm_df.groupby("equipment_id")["cycle"].max().add(1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `print(life_summary.describe())` | 결과를 콘솔에 출력합니다. |
| 20 | `sensor_summary = pm_df.groupby("failed")[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    ["temperature_c","vibration_rms_g","motor_current_a","particle_count","health_index"]` | 예지보전 분석 단계를 수행합니다. |
| 22 | `].mean()` | 예지보전 분석 단계를 수행합니다. |
| 23 | `print(sensor_summary.round(4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. RUL 라벨은 실제 고장 또는 교체 시점과 어떻게 연결되었는가?
2. 장비 단위 데이터 누수를 방지했는가?
3. 정비 임계값은 비용과 안전을 함께 반영하는가?