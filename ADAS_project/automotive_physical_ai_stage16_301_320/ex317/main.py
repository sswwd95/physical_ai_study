import pandas as pd
from common.control_utils import PID, simulate_first_order, error_metrics, output_path
rows=[]
for dt in [.1,.05,.02,.01]:
    m=error_metrics(simulate_first_order(PID(1.5,.7,.1,2.0,2.0),1.0,dt=dt))
    rows.append({"dt_s":dt,**m})
r=pd.DataFrame(rows)
p=output_path("ex317_sampling_period_comparison.csv"); r.to_csv(p,index=False,encoding="utf-8-sig")
print(r)
