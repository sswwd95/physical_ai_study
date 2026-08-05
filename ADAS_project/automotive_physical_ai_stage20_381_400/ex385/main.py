from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import model_path
env=SimpleCarEnv(max_steps=100)
model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=800)
p=model_path("ex385_ppo_car")
model.save(str(p))
print("saved:",p)
env.close()
