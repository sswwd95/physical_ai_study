import pandas as pd
from common.control_utils import PID, simulate_first_order, error_metrics, output_path
controllers = {
    "P": PID(1.5,0,0,2.0),
    "PI": PID(1.2,0.8,0,2.0,2.0),
    "PID": PID(1.5,0.7,0.12,2.0,2.0),
}
rows=[]
for name,c in controllers.items():
    m=error_metrics(simulate_first_order(c,1.0))
    rows.append({"controller":name,**m})
result=pd.DataFrame(rows)
p=output_path("ex305_controller_comparison.csv")
result.to_csv(p,index=False,encoding="utf-8-sig")
print(result)
