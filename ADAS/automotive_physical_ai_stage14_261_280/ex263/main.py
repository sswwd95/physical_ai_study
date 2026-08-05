from common.health_utils import load_data,moving_slope,output_path
df=load_data()
df["current_slope"]=moving_slope(df["motor_current_a"],100)
p=output_path("ex263_motor_current_slope.csv")
df[["time_s","motor_current_a","current_slope"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df["current_slope"].dropna().describe())
