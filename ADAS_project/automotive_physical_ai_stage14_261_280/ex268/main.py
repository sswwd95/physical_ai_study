from common.health_utils import load_data,output_path
df=load_data()
df["motor_temp_warn"]=df["motor_temp_c"]>70
df["vibration_warn"]=df["bearing_vibration_g"]>0.45
df["battery_warn"]=df["battery_voltage_v"]<11.9
df["resistance_warn"]=df["battery_internal_resistance_ohm"]>0.08
df["any_warning"]=df[["motor_temp_warn","vibration_warn","battery_warn","resistance_warn"]].any(axis=1)
p=output_path("ex268_component_warnings.csv")
df[df["any_warning"]].to_csv(p,index=False,encoding="utf-8-sig")
print(df[["motor_temp_warn","vibration_warn","battery_warn","resistance_warn"]].sum())
