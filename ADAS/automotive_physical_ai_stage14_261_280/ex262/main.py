from common.health_utils import load_data,output_path
df=load_data()
df["motor_temp_ma"]=df["motor_temp_c"].rolling(50,min_periods=1).mean()
p=output_path("ex262_motor_temp_trend.csv")
df[["time_s","motor_temp_c","motor_temp_ma"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df[["motor_temp_c","motor_temp_ma"]].tail())
