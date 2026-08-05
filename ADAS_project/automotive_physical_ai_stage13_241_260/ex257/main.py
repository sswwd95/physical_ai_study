from common.risk_utils import load_data,classification_metrics,save_json
df=load_data(); prob=df["true_risk_probability"].to_numpy(); y=df["risk_label"].to_numpy()
best=None
for th in [i/100 for i in range(5,96,5)]:
    m=classification_metrics(y,prob,th)
    m["cost"]=m["fn"]*10+m["fp"]*2
    if best is None or m["cost"]<best["cost"]: best=m
pth=save_json(best,"ex257_best_cost_threshold.json")
print(best); print(pth)
