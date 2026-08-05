import numpy as np
from common.health_utils import load_data,output_path
df=load_data()
df["health_level"]=np.select(
    [df["health_score"]<25,df["health_score"]<50,df["health_score"]<75],
    ["CRITICAL","POOR","CAUTION"],default="GOOD")
s=df["health_level"].value_counts().rename_axis("level").reset_index(name="samples")
p=output_path("ex269_health_levels.csv"); s.to_csv(p,index=False,encoding="utf-8-sig")
print(s)
