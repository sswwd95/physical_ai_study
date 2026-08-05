from common.health_utils import load_data,output_path
df=load_data()
df["voltage_drop"]=df["battery_voltage_v"].iloc[0]-df["battery_voltage_v"]
p=output_path("ex265_battery_voltage_drop.csv")
df[["time_s","battery_voltage_v","voltage_drop"]].to_csv(p,index=False,encoding="utf-8-sig")
print("final voltage drop:",df["voltage_drop"].iloc[-1])
