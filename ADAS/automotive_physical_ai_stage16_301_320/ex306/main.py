from common.control_utils import PID, simulate_first_order, output_path
pid=PID(kp=4.0,ki=1.0,kd=0.1,output_limit=1.2,integral_limit=3.0)
df=simulate_first_order(pid,target=2.0)
print("max control:",df["control"].abs().max())
p=output_path("ex306_output_saturation.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
