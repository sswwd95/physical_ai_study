import numpy as np
from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import safety_filter
env=SimpleCarEnv(max_steps=100)
model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=1000)
obs,_=env.reset(seed=4)
for _ in range(20):
    raw,_=model.predict(obs,deterministic=True)
    safe=safety_filter(raw,obs[4],obs[1])
    obs,r,term,trunc,info=env.step(safe)
    print("raw:",raw,"safe:",safe)
    if term or trunc: break
env.close()
