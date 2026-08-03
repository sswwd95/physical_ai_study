"""
반도체 Physical AI 하네스 엔지니어링 실습 046~050
Windows 10 / Anaconda / Pandas / scikit-learn
시계열 분할, 누출 방지, 전처리 재사용, 품질 리포트
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
META_PATH = OUTPUT_DIR / "time_split_metadata.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

# 1. 시간 순서를 유지한 상태에서 분할 비율을 정의한다.
train_ratio = 0.60
validation_ratio = 0.20

train_end = int(len(df) * train_ratio)
validation_end = int(
    len(df) * (train_ratio + validation_ratio)
)

# 2. 과거→현재→미래 순서로 데이터를 나눈다.
train_df = df.iloc[:train_end].copy()
validation_df = df.iloc[
    train_end:validation_end
].copy()
test_df = df.iloc[validation_end:].copy()

# 3. 각 데이터셋을 별도 파일로 저장한다.
train_path = OUTPUT_DIR / "train.csv"
validation_path = OUTPUT_DIR / "validation.csv"
test_path = OUTPUT_DIR / "test.csv"

train_df.to_csv(train_path, index=False, encoding="utf-8-sig")
validation_df.to_csv(
    validation_path,
    index=False,
    encoding="utf-8-sig",
)
test_df.to_csv(test_path, index=False, encoding="utf-8-sig")

# 4. 시간 경계와 행 수를 메타데이터로 저장한다.
metadata = {
    "total_rows": len(df),
    "train_rows": len(train_df),
    "validation_rows": len(validation_df),
    "test_rows": len(test_df),
    "train_start": str(train_df["timestamp"].min()),
    "train_end": str(train_df["timestamp"].max()),
    "validation_start": str(validation_df["timestamp"].min()),
    "validation_end": str(validation_df["timestamp"].max()),
    "test_start": str(test_df["timestamp"].min()),
    "test_end": str(test_df["timestamp"].max()),
}

META_PATH.write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(metadata, ensure_ascii=False, indent=2))
print("[완료] 시간 순서 기반 분할을 저장했습니다.")
