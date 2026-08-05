import pandas as pd
from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import safety_filter,output_path
env=SimpleCarEnv(max_steps=120)
model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64)
model.learn(total_timesteps=1200)
rows=[]
for filtered in [False,True]:
    for seed in range(8):
        obs,_=env.reset(seed=seed); total=0; collision=departure=False
        while True:
            action,_=model.predict(obs,deterministic=True)
            if filtered: action=safety_filter(action,obs[4],obs[1])
            obs,r,term,trunc,info=env.step(action); total+=r
            if term or trunc:
                collision=info.get("collision",False); departure=info.get("lane_departure",False); break
        rows.append({"filtered":filtered,"seed":seed,"return":total,"collision":collision,"lane_departure":departure})
df=pd.DataFrame(rows)
p=output_path("ex397_safety_filter_comparison.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print(df.groupby("filtered")[["return","collision","lane_departure"]].mean())
env.close()
