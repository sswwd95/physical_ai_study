import pandas as pd
from common.risk_utils import load_data,classification_metrics,output_path
df=load_data(); prob=df["true_risk_probability"].to_numpy(); y=df["risk_label"].to_numpy()
rows=[]
false_negative_cost=10
false_positive_cost=2
for th in [.1,.2,.3,.4,.5,.6,.7,.8,.9]:
    m=classification_metrics(y,prob,th)
    m["cost"]=m["fn"]*false_negative_cost+m["fp"]*false_positive_cost
    rows.append(m)
result=pd.DataFrame(rows).sort_values("cost")
pth=output_path("ex256_threshold_cost.csv"); result.to_csv(pth,index=False,encoding="utf-8-sig")
print(result.head()); print(pth)
