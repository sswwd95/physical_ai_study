from common.safety_utils import load_data,output_path
df=load_data()
df["relative_speed_check"]=df["ego_speed_mps"]-df["lead_speed_mps"]
df["closing_speed_check"]=df["relative_speed_check"].clip(lower=0)
p=output_path("ex342_relative_speed.csv")
df[["time_s","relative_speed_check","closing_speed_check"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df[["relative_speed_check","closing_speed_check"]].head())
