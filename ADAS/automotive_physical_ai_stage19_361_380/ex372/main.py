import numpy as np
from envs.simple_car_env import SimpleCarEnv
env=SimpleCarEnv(max_steps=50,seed=7)
obs,_=env.reset(seed=7)
total=0
for _ in range(50):
    action=env.action_space.sample()
    obs,reward,terminated,truncated,info=env.step(action)
    total+=reward
    if terminated or truncated:
        break
print("steps:",env.steps,"return:",total,"final:",obs)
env.close()
