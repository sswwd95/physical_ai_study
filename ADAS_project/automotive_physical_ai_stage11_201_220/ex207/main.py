import numpy as np
from common.anomaly_utils import load_data, output_path
df = load_data()
df["ttc_level"] = np.select(
    [df["ttc_s"] < 1.0, df["ttc_s"] < 2.0, df["ttc_s"] < 4.0],
    ["CRITICAL","WARNING","CAUTION"],
    default="NORMAL"
)
summary = df["ttc_level"].value_counts().rename_axis("level").reset_index(name="samples")
path = output_path("ex207_ttc_levels.csv")
summary.to_csv(path,index=False,encoding="utf-8-sig")
print(summary)
