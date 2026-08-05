from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import model_path
env=SimpleCarEnv()
p=model_path("ex385_ppo_car")
if not p.with_suffix(".zip").exists():
    model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64)
    model.learn(total_timesteps=300)
    model.save(str(p))
loaded=PPO.load(str(p),env=env)
print("loaded:",type(loaded).__name__)
env.close()
