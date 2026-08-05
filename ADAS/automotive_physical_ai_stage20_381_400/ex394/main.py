import pandas as pd
from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import evaluate_policy_manual,output_path
rows=[]
for lr in [1e-4,3e-4,1e-3]:
    env=SimpleCarEnv(max_steps=100)
    model=PPO("MlpPolicy",env,verbose=0,seed=42,learning_rate=lr,n_steps=128,batch_size=64)
    model.learn(total_timesteps=800)
    rows.append({"learning_rate":lr,**evaluate_policy_manual(model,env,episodes=5)})
    env.close()
df=pd.DataFrame(rows)
p=output_path("ex394_learning_rate_comparison.csv")
df.to_csv(p,index=False,encoding="utf-8-sig")
print(df)
