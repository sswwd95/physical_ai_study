from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from .rl_env import TrackingGainEnv
from .config import result_dir
def main():
 e=TrackingGainEnv(); check_env(e); m=PPO('MlpPolicy',e,verbose=1,seed=42,n_steps=256,batch_size=64); m.learn(total_timesteps=10000); m.save(result_dir()/'ppo_tracking_gain')
if __name__=='__main__':main()
