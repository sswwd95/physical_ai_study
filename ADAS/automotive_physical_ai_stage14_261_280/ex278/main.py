from common.health_utils import load_data,output_path
df=load_data()
last=df.iloc[-1]
scores={
"motor":max(0,(last["motor_temp_c"]-55)/20)*40+max(0,(last["motor_current_a"]-4)/3)*20,
"bearing":max(0,(last["bearing_vibration_g"]-0.25)/0.25)*60,
"battery":max(0,(12.2-last["battery_voltage_v"])/0.5)*30+max(0,(last["battery_internal_resistance_ohm"]-0.06)/0.03)*40,
"wheel":max(0,(last["wheel_friction_index"]-0.15)/0.08)*40}
ranking=sorted(scores.items(),key=lambda x:x[1],reverse=True)
p=output_path("ex278_maintenance_priority.json")
p.write_text(__import__("json").dumps({"scores":scores,"ranking":ranking},indent=2),encoding="utf-8")
print(ranking)
