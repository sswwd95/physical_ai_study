import gymnasium as gym
from envs.simple_car_env import SimpleCarEnv
envs=gym.vector.SyncVectorEnv([lambda:SimpleCarEnv(seed=i) for i in range(4)])
obs,info=envs.reset(seed=42)
print("batch observation shape:",obs.shape)
actions=envs.action_space.sample()
next_obs,reward,terminated,truncated,info=envs.step(actions)
print(reward,terminated,truncated)
envs.close()
