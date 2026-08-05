from common.safety_utils import load_data,confusion_counts
df=load_data()
pred=(df["ttc_s"]<2.5)|(df["distance_m"]<df["safe_distance_m"])
c=confusion_counts(df["risk_label"],pred)
precision=c["tp"]/max(1,c["tp"]+c["fp"])
recall=c["tp"]/max(1,c["tp"]+c["fn"])
print(c)
print("precision:",precision,"recall:",recall)
