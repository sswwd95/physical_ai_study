from common.reliability_utils import load_lifetime, output_path
df=load_lifetime()
s=df.groupby("component")["observed_time_h"].agg(["count","mean","std","min","max"])
p=output_path("ex282_lifetime_summary.csv")
s.to_csv(p,encoding="utf-8-sig")
print(s)
