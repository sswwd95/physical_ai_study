from common.reliability_utils import load_lifetime
df=load_lifetime()
print(df.head())
print(df.groupby("component")["failure_event"].agg(["count","sum","mean"]))
