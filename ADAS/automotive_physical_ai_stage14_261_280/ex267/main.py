from common.health_utils import load_data,output_path
df=load_data()
threshold=df["wheel_friction_index"].quantile(.95)
events=df[df["wheel_friction_index"]>threshold]
p=output_path("ex267_high_friction_events.csv")
events.to_csv(p,index=False,encoding="utf-8-sig")
print("threshold:",threshold,"events:",len(events))
