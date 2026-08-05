from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import evaluate_policy_manual
env=SimpleCarEnv(max_steps=120)
model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=1200)
print(evaluate_policy_manual(model,env,episodes=8,deterministic=True))
env.close()
