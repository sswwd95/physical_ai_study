from common.safety_utils import load_data,hysteresis_alarm,output_path
df=load_data()
df["ttc_warning"]=hysteresis_alarm(df["ttc_s"],on_threshold=2.0,off_threshold=3.0)
p=output_path("ex351_hysteresis_warning.csv")
df[["time_s","ttc_s","ttc_warning"]].to_csv(p,index=False,encoding="utf-8-sig")
print("warning transitions:",int((df["ttc_warning"]!=df["ttc_warning"].shift()).sum()))
