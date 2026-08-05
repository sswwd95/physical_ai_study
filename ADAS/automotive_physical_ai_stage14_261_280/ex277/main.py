from common.health_utils import load_data,output_path
df=load_data()
recent=df.tail(500)
slope=__import__("numpy").polyfit(recent["time_s"],recent["health_score"],1)[0]
current=float(recent["health_score"].iloc[-1]); limit=30.0
rul=(limit-current)/slope if slope<0 else float("inf")
result={"current_health":current,"health_limit":limit,"slope_per_s":float(slope),"estimated_rul_s":float(rul)}
p=output_path("ex277_health_rul.json"); p.write_text(__import__("json").dumps(result,indent=2),encoding="utf-8")
print(result)
