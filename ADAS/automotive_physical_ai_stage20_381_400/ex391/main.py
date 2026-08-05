from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import CheckpointCallback
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import model_path
env=SimpleCarEnv(max_steps=100)
callback=CheckpointCallback(save_freq=300,save_path=str(model_path("ex391_checkpoints")),name_prefix="ppo_car")
model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=900,callback=callback)
print("checkpoint complete")
env.close()
