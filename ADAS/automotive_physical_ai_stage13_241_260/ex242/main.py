from common.risk_utils import load_data
df=load_data()
print(df["true_risk_probability"].describe())
print(df.groupby("severity")["true_risk_probability"].agg(["count","mean","min","max"]))
