from common.health_utils import load_data,output_path
df=load_data()
baseline=df.loc[df["time_s"]<300,"bearing_vibration_g"]
threshold=baseline.mean()+4*baseline.std()
idx=df.index[df["bearing_vibration_g"]>threshold]
start_time=float(df.loc[idx[0],"time_s"]) if len(idx) else None
result={"threshold":float(threshold),"degradation_start_s":start_time}
p=output_path("ex270_degradation_start.json")
p.write_text(__import__("json").dumps(result,indent=2),encoding="utf-8")
print(result)
