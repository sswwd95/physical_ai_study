from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv,VecNormalize
from envs.simple_car_env import SimpleCarEnv
venv=DummyVecEnv([lambda:SimpleCarEnv(max_steps=100)])
venv=VecNormalize(venv,norm_obs=True,norm_reward=True,clip_obs=10)
model=PPO("MlpPolicy",venv,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=800)
print("obs mean:",venv.obs_rms.mean)
venv.close()
