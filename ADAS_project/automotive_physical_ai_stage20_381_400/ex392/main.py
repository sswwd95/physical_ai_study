from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from envs.simple_car_env import SimpleCarEnv
vec_env=make_vec_env(SimpleCarEnv,n_envs=4,seed=42,env_kwargs={"max_steps":100})
model=PPO("MlpPolicy",vec_env,verbose=0,seed=42,n_steps=128,batch_size=128)
model.learn(total_timesteps=1200)
print("vector training complete")
vec_env.close()
