from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import output_path,model_path
train_env=SimpleCarEnv(max_steps=100)
eval_env=SimpleCarEnv(max_steps=100,seed=99)
callback=EvalCallback(eval_env,best_model_save_path=str(model_path("ex390_best")),
                      log_path=str(output_path("ex390_eval")),eval_freq=250,
                      n_eval_episodes=3,deterministic=True)
model=PPO("MlpPolicy",train_env,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=1000,callback=callback)
print("evaluation callback complete")
train_env.close(); eval_env.close()
