from common.control_utils import PID, simulate_first_order, output_path
def target(t): return 3.0 if t<4 else 0.3
pid=PID(1.4,1.0,0.05,output_limit=1.0,integral_limit=1.5)
df=simulate_first_order(pid,target=target,duration=9)
print("max integral:",df["integral"].abs().max())
p=output_path("ex308_anti_windup.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
