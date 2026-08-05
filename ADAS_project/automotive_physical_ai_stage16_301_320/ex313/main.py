from common.control_utils import PID, simulate_first_order, error_metrics, output_path
pid=PID(2.0,0.8,0.15,output_limit=2.5,integral_limit=2.0)
df=simulate_first_order(pid,target=0.7,tau=.40)
print(error_metrics(df))
p=output_path("ex313_yaw_rate_pid.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
