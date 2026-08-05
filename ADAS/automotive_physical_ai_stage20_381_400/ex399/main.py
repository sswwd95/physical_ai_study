import pandas as pd,numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import output_path
class RewardCallback(BaseCallback):
    def __init__(self):
        super().__init__(); self.steps=[]; self.rewards=[]
    def _on_step(self):
        self.steps.append(self.num_timesteps)
        self.rewards.append(float(np.mean(self.locals["rewards"])))
        return True
env=SimpleCarEnv(max_steps=100)
cb=RewardCallback()
model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=1200,callback=cb)
df=pd.DataFrame({"step":cb.steps,"reward":cb.rewards})
csvp=output_path("ex399_training_curve.csv"); df.to_csv(csvp,index=False,encoding="utf-8-sig")
fig,ax=plt.subplots(figsize=(9,4)); ax.plot(df["step"],df["reward"].rolling(50,min_periods=1).mean()); ax.grid(True); ax.set_xlabel("Step"); ax.set_ylabel("Mean reward")
pngp=output_path("ex399_training_curve.png"); fig.tight_layout(); fig.savefig(pngp,dpi=140); plt.close(fig)
print(csvp,pngp)
env.close()
