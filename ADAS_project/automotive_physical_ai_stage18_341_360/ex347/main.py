from common.safety_utils import load_data,output_path
df=load_data()
df["unsafe_distance"]=df["distance_m"]<df["safe_distance_m"]
p=output_path("ex347_unsafe_distance.csv")
df[df["unsafe_distance"]].to_csv(p,index=False,encoding="utf-8-sig")
print("unsafe samples:",int(df["unsafe_distance"].sum()))
