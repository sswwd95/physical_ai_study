import numpy as np
from envs.simple_car_env import SimpleCarEnv
env=SimpleCarEnv(max_steps=80,seed=3)
obs,_=env.reset(seed=3)
total=0
for _ in range(80):
    steering=np.clip(-1.2*obs[1]-0.8*obs[2],-1,1)
    action=np.array([.45,steering],dtype=np.float32)
    obs,reward,terminated,truncated,info=env.step(action)
    total+=reward
    if terminated or truncated: break
print("steps:",env.steps,"return:",total,"final:",obs)
env.close()
