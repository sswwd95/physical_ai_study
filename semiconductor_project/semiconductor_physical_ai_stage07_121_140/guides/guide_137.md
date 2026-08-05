# 실습 137 — low_confidence_review

## 1. 학습 목표
최대 예측확률이 낮은 행을 자동 판정하지 않고 재검사 대상으로 분리합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
보정된 다중 클래스 모델의 predict_proba를 사용하라.
최대 확률이 0.55 미만이면 review_required=True로 표시하고
상위 두 클래스와 확률 차이도 계산하여 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage07
python examples\ex137_low_confidence_review.py
```

## 4. 예상 결과
확신도가 낮은 예측이 재검사 대상으로 분리됩니다.

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
| 15 | `from sklearn.calibration import CalibratedClassifierCV` | 필요한 라이브러리나 모델을 불러옵니다. |
| 16 | `from sklearn.compose import ColumnTransformer` | 필요한 라이브러리나 모델을 불러옵니다. |
| 17 | `from sklearn.ensemble import RandomForestClassifier` | 필요한 라이브러리나 모델을 불러옵니다. |
| 18 | `from sklearn.model_selection import train_test_split` | 필요한 라이브러리나 모델을 불러옵니다. |
| 19 | `from sklearn.pipeline import Pipeline` | 필요한 라이브러리나 모델을 불러옵니다. |
| 20 | `from sklearn.preprocessing import OneHotEncoder` | 필요한 라이브러리나 모델을 불러옵니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 다중 불량 유형 CSV를 DataFrame으로 읽습니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `feature_columns = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    "recipe",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 26 | `    "chamber_id",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 27 | `    "chamber_temp_c",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 28 | `    "chamber_pressure_pa",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 29 | `    "rf_power_w",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 30 | `    "gas_flow_sccm",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 31 | `    "vibration_g",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 32 | `    "particle_count",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 33 | `    "etch_rate_nm_min",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 34 | `    "uniformity_percent",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 35 | `]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 36 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 37 | `x = sensor_df[feature_columns]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `y = sensor_df["defect_type"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 39 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 40 | `train_index, test_index = train_test_split(` | 학습용과 평가용 데이터를 분리합니다. |
| 41 | `    np.arange(len(sensor_df)),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 42 | `    test_size=0.25,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `    stratify=y,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 46 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 47 | `x_train = x.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `x_test = x.iloc[test_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 49 | `y_train = y.iloc[train_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 51 | `preprocessor = ColumnTransformer([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `    ("num", "passthrough", feature_columns[2:]),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 53 | `    ("cat", OneHotEncoder(handle_unknown="ignore"), feature_columns[:2]),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 54 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 55 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 56 | `base_model = Pipeline([` | 계산 결과나 설정값을 변수에 저장합니다. |
| 57 | `    ("preprocess", preprocessor),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 58 | `    (` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 59 | `        "classifier",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 60 | `        RandomForestClassifier(` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 61 | `            n_estimators=300,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `            class_weight="balanced",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `            random_state=42,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `            n_jobs=-1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 65 | `        ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 66 | `    ),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 67 | `])` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 68 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 69 | `model = CalibratedClassifierCV(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 70 | `    estimator=base_model,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `    method="sigmoid",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `    cv=3,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 73 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 74 | `model.fit(x_train, y_train)` | 학습 데이터로 전처리기와 모델을 학습합니다. |
| 75 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 76 | `probability = model.predict_proba(x_test)` | 각 불량 유형에 속할 확률을 계산합니다. |
| 77 | `order = np.argsort(probability, axis=1)[:, ::-1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 78 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 79 | `top1_index = order[:, 0]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 80 | `top2_index = order[:, 1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 81 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 82 | `result_df = sensor_df.iloc[test_index][` | 계산 결과나 설정값을 변수에 저장합니다. |
| 83 | `    ["timestamp", "lot_id", "defect_type"]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 84 | `].copy()` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 85 | `result_df["predicted_class"] = model.classes_[top1_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 86 | `result_df["top1_probability"] = probability[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 87 | `    np.arange(len(probability)),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 88 | `    top1_index,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 89 | `]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 90 | `result_df["top2_class"] = model.classes_[top2_index]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 91 | `result_df["top2_probability"] = probability[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 92 | `    np.arange(len(probability)),` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 93 | `    top2_index,` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 94 | `]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 95 | `result_df["probability_gap"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 96 | `    result_df["top1_probability"]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 97 | `    - result_df["top2_probability"]` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 98 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 99 | `result_df["review_required"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 100 | `    result_df["top1_probability"] < 0.55` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 101 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 102 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 103 | `print("재검사 대상 수:", int(result_df["review_required"].sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 104 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 105 | `    OUTPUT_DIR / "ex137_low_confidence_review.csv",` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |
| 106 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 107 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 108 | `)` | 다중 클래스 분류 또는 모델 튜닝 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 가장 희소한 불량 유형의 재현율이 낮으면 어떤 위험이 있는가?
2. macro F1과 weighted F1 중 어떤 지표가 더 적합한가?
3. 클래스 확률이 낮을 때 보류 또는 재검사 정책을 어떻게 설계할 것인가?