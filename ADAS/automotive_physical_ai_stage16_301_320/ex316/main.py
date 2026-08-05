import pandas as pd
from common.control_utils import PID, simulate_first_order, error_metrics, output_path
rows=[]
for kp in [0.8,1.2,1.6,2.0]:
    for ki in [0.0,0.4,0.8]:
        for kd in [0.0,0.08,0.16]:
            m=error_metrics(simulate_first_order(PID(kp,ki,kd,2.0,2.0),1.0))
            rows.append({"kp":kp,"ki":ki,"kd":kd,**m})
r=pd.DataFrame(rows).sort_values("rmse")
p=output_path("ex316_pid_grid_search.csv"); r.to_csv(p,index=False,encoding="utf-8-sig")
print(r.head())
