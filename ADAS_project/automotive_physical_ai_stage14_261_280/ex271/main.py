from sklearn.linear_model import LinearRegression
from common.health_utils import load_data,rmse,output_path
df=load_data(); split=int(len(df)*.7)
model=LinearRegression().fit(df.iloc[:split][["time_s"]],df.iloc[:split]["motor_temp_c"])
pred=model.predict(df.iloc[split:][["time_s"]])
print("RMSE:",rmse(df.iloc[split:]["motor_temp_c"],pred))
out=df.iloc[split:][["time_s","motor_temp_c"]].copy(); out["predicted_temp_c"]=pred
p=output_path("ex271_motor_temp_prediction.csv"); out.to_csv(p,index=False,encoding="utf-8-sig")
