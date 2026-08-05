from common.safety_utils import load_data,output_path
df=load_data()
df["emergency_stop"]=(df["ttc_s"]<1.0)|(df["distance_m"]<2.5)
p=output_path("ex350_emergency_stop.csv")
df[df["emergency_stop"]].to_csv(p,index=False,encoding="utf-8-sig")
print("emergency samples:",int(df["emergency_stop"].sum()))
