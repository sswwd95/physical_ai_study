# 실습 204 — sensor_feature_engineering

## 1. 학습 목표
센서 비율과 복합 특징을 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
진동 peak/rms, 압력/펌프속도, 열부하, 입자/유량 특징을 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage11
python examples\ex204_sensor_feature_engineering.py
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
| 15 | `sensor_df=pd.read_csv(DATA_FILE)` | 장비 상태 진단 CSV를 DataFrame으로 읽습니다. |
| 16 | `sensor_df["peak_to_rms"]=sensor_df["vibration_peak_g"]/sensor_df["vibration_rms_g"].replace(0,np.nan)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `sensor_df["pressure_speed_ratio"]=sensor_df["pressure_pa"]/sensor_df["pump_speed_rpm"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `sensor_df["thermal_load"]=sensor_df["temperature_c"]*sensor_df["motor_current_a"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `sensor_df["particle_per_flow"]=sensor_df["particle_count"]/sensor_df["gas_flow_sccm"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `print(sensor_df[["peak_to_rms","pressure_speed_ratio","thermal_load","particle_per_flow"]].describe().round(4))` | 결과를 콘솔에 출력합니다. |
| 21 | `sensor_df.to_csv(OUTPUT_DIR/"ex204_engineered_features.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 고장 라벨은 정비 이력과 어떤 규칙으로 연결되었는가?
2. 장비별 편차와 운전모드 차이를 모델이 구분하는가?
3. 고장 확률이 낮을 때 자동 정지보다 재검사가 적절한가?