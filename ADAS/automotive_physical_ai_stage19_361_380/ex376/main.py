from envs.simple_car_env import SimpleCarEnv
e1=SimpleCarEnv(seed=42); e2=SimpleCarEnv(seed=42)
o1,_=e1.reset(seed=123); o2,_=e2.reset(seed=123)
print(o1); print(o2); print("equal:",(o1==o2).all())
e1.close(); e2.close()
