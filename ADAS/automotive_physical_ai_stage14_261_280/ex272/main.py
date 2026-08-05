from sklearn.ensemble import RandomForestRegressor
from common.health_utils import load_data,FEATURES,rmse,output_path
df=load_data(); split=int(len(df)*.7)
model=RandomForestRegressor(n_estimators=150,random_state=42,n_jobs=1)
model.fit(df.iloc[:split][FEATURES],df.iloc[:split]["health_score"])
pred=model.predict(df.iloc[split:][FEATURES])
print("RMSE:",rmse(df.iloc[split:]["health_score"],pred))
out=df.iloc[split:][["time_s","health_score"]].copy(); out["predicted_health"]=pred
p=output_path("ex272_health_prediction.csv"); out.to_csv(p,index=False,encoding="utf-8-sig")
