from common.health_utils import load_data,moving_slope,output_path
df=load_data()
df["resistance_slope"]=moving_slope(df["battery_internal_resistance_ohm"],120)
p=output_path("ex266_internal_resistance_slope.csv")
df[["time_s","battery_internal_resistance_ohm","resistance_slope"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df["resistance_slope"].dropna().tail())
