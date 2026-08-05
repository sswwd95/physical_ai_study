from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_multiclass_defects.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_multiclass_defects.csv 파일이 없습니다."
    )

from sklearn.preprocessing import LabelEncoder

sensor_df = pd.read_csv(DATA_FILE)

encoder = LabelEncoder()
encoded = encoder.fit_transform(sensor_df["defect_type"])

mapping_df = pd.DataFrame({
    "class_name": encoder.classes_,
    "encoded_value": np.arange(len(encoder.classes_)),
})

print(mapping_df)
print("처음 10개 정수 라벨:", encoded[:10])
print(
    "역변환 예시:",
    encoder.inverse_transform(encoded[:10]),
)

mapping_df.to_csv(
    OUTPUT_DIR / "ex122_label_mapping.csv",
    index=False,
    encoding="utf-8-sig",
)
