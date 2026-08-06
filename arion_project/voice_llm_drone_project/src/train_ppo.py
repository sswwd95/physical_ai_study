from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from .rl_env import SafetyTuningEnv
from .config import result_dir
def main():
    env=SafetyTuningEnv(); check_env(env); model=PPO('MlpPolicy',env,verbose=1,seed=42,n_steps=256,batch_size=64); model.learn(10000); model.save(result_dir()/'ppo_safety_tuner')
if __name__=='__main__': main()
