from common.control_utils import PID, simulate_first_order, error_metrics, output_path
pid = PID(kp=1.2, ki=0.8, output_limit=2.0, integral_limit=2.0)
df = simulate_first_order(pid, target=1.0)
p = output_path("ex303_pi_speed_response.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
print(error_metrics(df)); print(p)
