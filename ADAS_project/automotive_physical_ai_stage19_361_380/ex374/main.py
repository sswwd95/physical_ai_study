import pandas as pd,numpy as np
from envs.simple_car_env import SimpleCarEnv
from common.rl_utils import output_path
env=SimpleCarEnv(max_steps=60,seed=11)
obs,_=env.reset(seed=11); rows=[]
for _ in range(60):
    action=np.array([.4,np.clip(-obs[1]-obs[2],-1,1)],dtype=np.float32)
    obs,reward,terminated,truncated,info=env.step(action)
    rows.append({"step":env.steps,"reward":reward,**info})
    if terminated or truncated: break
df=pd.DataFrame(rows)
p=output_path("ex374_reward_components.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print(df.sum(numeric_only=True)); print(p)
env.close()
