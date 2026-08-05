import numpy as np,pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from envs.simple_car_env import SimpleCarEnv
from common.rl_utils import output_path
returns=[]
for seed in range(20):
    env=SimpleCarEnv(max_steps=80,seed=seed); obs,_=env.reset(seed=seed); total=0
    for _ in range(80):
        action=np.array([.45,np.clip(-1.2*obs[1]-.8*obs[2],-1,1)],dtype=np.float32)
        obs,r,term,trunc,_=env.step(action); total+=r
        if term or trunc: break
    returns.append(total); env.close()
fig,ax=plt.subplots(figsize=(8,4)); ax.plot(returns,marker="o"); ax.grid(True); ax.set_xlabel("Episode"); ax.set_ylabel("Return")
p=output_path("ex379_episode_returns.png"); fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print(pd.Series(returns).describe()); print(p)
