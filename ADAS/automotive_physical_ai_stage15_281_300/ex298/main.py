import numpy as np
from common.reliability_utils import load_rul,save_json
df=load_rul()
threshold=200
prob=float(np.mean(df["observed_rul_h"]<threshold))
result={"threshold_h":threshold,"empirical_probability_rul_below_threshold":prob}
print(result); print(save_json(result,"ex298_maintenance_threshold_probability.json"))
