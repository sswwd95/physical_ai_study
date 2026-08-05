import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import output_path
env=SimpleCarEnv(max_steps=100)
model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=1000)
actions=[]
for seed in range(10):
    obs,_=env.reset(seed=seed)
    for _ in range(60):
        action,_=model.predict(obs,deterministic=False)
        actions.append(action)
        obs,r,term,trunc,info=env.step(action)
        if term or trunc: break
actions=np.asarray(actions)
fig,ax=plt.subplots(figsize=(7,5))
ax.scatter(actions[:,0],actions[:,1],s=10,alpha=.5)
ax.set_xlabel("Throttle"); ax.set_ylabel("Steering"); ax.grid(True)
p=output_path("ex398_action_distribution.png")
fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)
print(p)
env.close()
