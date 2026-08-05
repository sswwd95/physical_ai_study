from common.control_utils import PID, simulate_first_order, error_metrics, output_path
pid = PID(kp=1.5, ki=0.7, kd=0.12, output_limit=2.0, integral_limit=2.0)
df = simulate_first_order(pid, target=1.0)
p = output_path("ex304_pid_speed_response.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
print(error_metrics(df)); print(p)
