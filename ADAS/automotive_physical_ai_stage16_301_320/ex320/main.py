import json, pandas as pd
from common.control_utils import PID, simulate_first_order, error_metrics, output_path
def target(t):
    if t<2:return 0.0
    if t<6:return 0.8
    if t<10:return 1.2
    if t<13:return 0.5
    return 0.0
def disturbance(t): return -0.45 if 7<t<8.5 else 0.0
pid=PID(1.5,.75,.1,2.0,2.0)
df=simulate_first_order(pid,target,duration=15,dt=.02,deadzone=.05,disturbance=disturbance)
csv_path=output_path("ex320_integrated_pid_log.csv")
df.to_csv(csv_path,index=False,encoding="utf-8-sig")
m=error_metrics(df)
m.update({"kp":pid.kp,"ki":pid.ki,"kd":pid.kd,"output_limit":pid.output_limit,"integral_limit":pid.integral_limit})
json_path=output_path("ex320_integrated_report.json")
json_path.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding="utf-8")
print(m); print(csv_path,json_path)
