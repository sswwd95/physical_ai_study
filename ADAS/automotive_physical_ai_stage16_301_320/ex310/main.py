from common.control_utils import PID, simulate_first_order, output_path
def target(t):
    if t<2: return 0.0
    if t<5: return 0.7
    if t<7: return 1.2
    return 0.4
pid=PID(1.5,0.7,0.1,2.0,2.0)
df=simulate_first_order(pid,target,duration=10)
p=output_path("ex310_step_reference_tracking.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
print(df.tail())
