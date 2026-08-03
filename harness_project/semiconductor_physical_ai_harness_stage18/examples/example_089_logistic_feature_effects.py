"""
반도체 Physical AI 하네스 엔지니어링 실습 086~090
Windows 10 / Anaconda / Pandas / scikit-learn
로지스틱 회귀 기반 불량 예측
"""

from pathlib import Path
import joblib
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "logistic_defect_model.joblib"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "logistic_feature_effects.csv"

model = joblib.load(MODEL_PATH)

preprocessor = model.named_steps["preprocessor"]
classifier = model.named_steps["classifier"]

# 1. 전처리 이후 실제 특징 이름을 가져온다.
feature_names = list(
    preprocessor.get_feature_names_out()
)

coefficients = classifier.coef_[0]

# 2. 계수와 오즈비를 계산한다.
result = pd.DataFrame(
    {
        "feature": feature_names,
        "coefficient": coefficients,
        "absolute_coefficient": np.abs(coefficients),
        "odds_ratio": np.exp(coefficients),
    }
)

# 3. 계수 방향을 사람이 읽기 쉽게 표시한다.
def effect_direction(value):
    if value > 0:
        return "INCREASE_DEFECT_ODDS"
    if value < 0:
        return "DECREASE_DEFECT_ODDS"
    return "NO_EFFECT"

result["effect_direction"] = (
    result["coefficient"]
    .apply(effect_direction)
)

result = result.sort_values(
    "absolute_coefficient",
    ascending=False,
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result.head(15).round(5))
print()
print(
    "주의: 계수와 오즈비는 모델 내 연관성이지 "
    "공정 인과관계의 확정이 아닙니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
