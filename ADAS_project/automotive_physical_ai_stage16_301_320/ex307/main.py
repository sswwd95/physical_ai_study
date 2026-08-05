from common.control_utils import PID, simulate_first_order, error_metrics, output_path
pid=PID(1.2,0.5,0.05,output_limit=2.0,integral_limit=2.0)
df=simulate_first_order(pid,target=0.3,deadzone=0.18)
print(error_metrics(df))
p=output_path("ex307_deadzone_response.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
