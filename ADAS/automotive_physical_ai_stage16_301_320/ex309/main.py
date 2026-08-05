from common.control_utils import PID, simulate_first_order, error_metrics, output_path
def disturbance(t): return -0.55 if 3<=t<5 else 0.0
pid=PID(1.5,0.8,0.1,output_limit=2.0,integral_limit=2.0)
df=simulate_first_order(pid,1.0,disturbance=disturbance)
print(error_metrics(df))
p=output_path("ex309_disturbance_rejection.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
