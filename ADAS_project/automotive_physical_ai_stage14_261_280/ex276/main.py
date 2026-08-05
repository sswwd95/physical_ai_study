from common.health_utils import load_data,output_path
df=load_data()
threshold=70.0
recent=df.tail(400)
slope=__import__("numpy").polyfit(recent["time_s"],recent["motor_temp_c"],1)[0]
current=float(recent["motor_temp_c"].iloc[-1])
rul=(threshold-current)/slope if slope>0 else float("inf")
result={"temperature_threshold_c":threshold,"current_temp_c":current,"slope_c_per_s":float(slope),"estimated_rul_s":float(rul)}
p=output_path("ex276_simple_rul.json"); p.write_text(__import__("json").dumps(result,indent=2),encoding="utf-8")
print(result)
