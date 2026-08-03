# 실습 138 — misclassification_analysis

## 1. 학습 목표
오분류 행을 실제·예측 클래스 쌍별로 집계합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
RandomForest 평가 결과에서 actual_class != predicted_class인 행만 추출하라.
실제→예측 클래스 조합별 건수를 집계하고 상세 오분류 행과 함께 CSV 두 개로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex138_misclassification_analysis.py
```

## 4. 예상 결과
자주 발생하는 오분류 방향과 상세 센서값이 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_multiclass_defects.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 12 | `        "data/semiconductor_multiclass_defects.csv 파일이 없습니다."` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 13 | `    )` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 21 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `feature_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    "recipe",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 25 | `    "chamber_id",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 26 | `    "chamber_temp_c",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 27 | `    "chamber_pressure_pa",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 28 | `    "rf_power_w",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 29 | `    "gas_flow_sccm",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 30 | `    "vibration_g",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 31 | `    "particle_count",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 32 | `    "etch_rate_nm_min",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 33 | `    "uniformity_percent",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 34 | `]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 35 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 36 | `x = sensor_df[feature_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `y = sensor_df["defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `train_index, test_index = train_test_split(` | 학습용과 평가용 데이터를 분리합니다. |
| 40 | `    np.arange(len(sensor_df)),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 41 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    stratify=y,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 45 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 46 | `preprocessor = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `    ("num", "passthrough", feature_columns[2:]),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 48 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), feature_columns[:2]),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 50 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 51 | `model = Pipeline([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `    ("preprocess", preprocessor),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 53 | `    (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 54 | `        "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 55 | `        RandomForestClassifier(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 56 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 58 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 61 | `    ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 62 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 63 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 64 | `model.fit(x.iloc[train_index], y.iloc[train_index])` | 학습 데이터로 전처리기와 모델을 학습합니다. |
| 65 | `prediction = model.predict(x.iloc[test_index])` | 학습된 모델로 불량 유형을 예측합니다. |
| 66 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 67 | `result_df = sensor_df.iloc[test_index].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `result_df["predicted_class"] = prediction` | 계산 결과나 설정값을 변수에 저장합니다. |
| 69 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 70 | `error_df = result_df.loc[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `    result_df["defect_type"] != result_df["predicted_class"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `].copy()` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 73 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 74 | `pair_summary = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `    error_df.groupby(["defect_type", "predicted_class"])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 76 | `    .size()` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 77 | `    .rename("error_count")` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 78 | `    .reset_index()` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 79 | `    .sort_values("error_count", ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 80 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 81 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 82 | `print(pair_summary)` | 실행 결과를 콘솔에 출력합니다. |
| 83 | `error_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 84 | `    OUTPUT_DIR / "ex138_misclassified_rows.csv",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 85 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 86 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 87 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 88 | `pair_summary.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 89 | `    OUTPUT_DIR / "ex138_error_pair_summary.csv",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 90 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 91 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 92 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?