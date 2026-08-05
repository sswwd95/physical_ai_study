# 실습 201 — fault_data_profile

## 1. 학습 목표
고장 유형과 센서 분포를 확인합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
고장 유형별 건수와 센서 평균을 비교하는 pandas 예제를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage11
python examples\ex201_fault_data_profile.py
```

## 4. 예상 결과
요청한 장비 상태 진단 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 분류 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "equipment_fault_diagnosis.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 12 | `        "data/equipment_fault_diagnosis.csv 파일이 없습니다."` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 13 | `    )` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `sensor_df = pd.read_csv(DATA_FILE)` | 장비 상태 진단 CSV를 DataFrame으로 읽습니다. |
| 16 | `print("데이터 크기:", sensor_df.shape)` | 결과를 콘솔에 출력합니다. |
| 17 | `print(sensor_df["fault_type"].value_counts())` | 결과를 콘솔에 출력합니다. |
| 18 | `summary = sensor_df.groupby("fault_type")[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    ["temperature_c","pressure_pa","vibration_rms_g","motor_current_a","particle_count"]` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 20 | `].mean()` | 장비 상태 진단 또는 고장 분류 단계를 수행합니다. |
| 21 | `print(summary.round(3))` | 결과를 콘솔에 출력합니다. |
| 22 | `summary.to_csv(OUTPUT_DIR/"ex201_fault_summary.csv",encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 고장 라벨은 정비 이력과 어떤 규칙으로 연결되었는가?
2. 장비별 편차와 운전모드 차이를 모델이 구분하는가?
3. 고장 확률이 낮을 때 자동 정지보다 재검사가 적절한가?