import json
from stable_baselines3 import PPO
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import evaluate_policy_manual,safety_filter,output_path,model_path
env=SimpleCarEnv(max_steps=120)
model=PPO("MlpPolicy",env,verbose=0,seed=42,n_steps=128,batch_size=64,
          learning_rate=3e-4,gamma=.99,gae_lambda=.95,clip_range=.2)
model.learn(total_timesteps=1800)
model_file=model_path("ex400_final_ppo")
model.save(str(model_file))
base=evaluate_policy_manual(model,env,episodes=10,deterministic=True)

returns=[]; collisions=departures=0
for seed in range(10):
    obs,_=env.reset(seed=seed); total=0
    while True:
        action,_=model.predict(obs,deterministic=True)
        action=safety_filter(action,obs[4],obs[1])
        obs,r,term,trunc,info=env.step(action); total+=r
        if term or trunc:
            collisions+=int(info.get("collision",False))
            departures+=int(info.get("lane_departure",False))
            break
    returns.append(total)
safe={
    "episodes":10,
    "mean_return":float(__import__("numpy").mean(returns)),
    "std_return":float(__import__("numpy").std(returns)),
    "collisions":collisions,
    "lane_departures":departures}
report={
    "training_timesteps":1800,
    "algorithm":"PPO",
    "policy":"MlpPolicy",
    "base_evaluation":base,
    "safety_filtered_evaluation":safe,
    "saved_model":str(model_file.with_suffix(".zip"))
}
p=output_path("ex400_integrated_report.json")
p.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report); print(p)
env.close()
