from common.safety_utils import load_data,risk_level,output_path
df=load_data()
df["risk_level"]=[risk_level(d,s,t) for d,s,t in zip(df["distance_m"],df["safe_distance_m"],df["ttc_s"])]
s=df["risk_level"].value_counts().rename_axis("level").reset_index(name="samples")
p=output_path("ex348_risk_levels.csv"); s.to_csv(p,index=False,encoding="utf-8-sig")
print(s)
