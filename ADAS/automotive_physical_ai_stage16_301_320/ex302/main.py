from common.control_utils import PID, simulate_first_order, error_metrics, output_path
pid = PID(kp=1.5, output_limit=2.0)
df = simulate_first_order(pid, target=1.0)
p = output_path("ex302_p_speed_response.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
print(error_metrics(df)); print(p)
