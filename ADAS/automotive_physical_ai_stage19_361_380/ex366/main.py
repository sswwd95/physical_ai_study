import numpy as np
from envs.simple_car_env import SimpleCarEnv
env=SimpleCarEnv(seed=42)
obs,_=env.reset(seed=42)
next_obs,reward,terminated,truncated,info=env.step(np.array([.5,.1],dtype=np.float32))
print(obs)
print(next_obs,reward,terminated,truncated,info)
env.close()
