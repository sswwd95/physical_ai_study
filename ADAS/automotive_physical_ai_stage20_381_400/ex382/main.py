from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
env=SimpleCarEnv()
model=PPO("MlpPolicy",env,verbose=0,seed=42)
print(model.policy)
env.close()
